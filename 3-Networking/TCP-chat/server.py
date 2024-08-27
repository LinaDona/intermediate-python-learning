import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

# helper function to broadcast meassages to users
def broadcast(message):
    for client in clients:
        client.send(message)

'''
Notice that we are always encoding and decoding the messages here. 
The reason for this is that we can only send bytes and not strings. 
So we always need to encode messages (for example using ASCII), when 
we send them and decode them, when we receive them.
'''

def handle(client):
    while True:
        try:
            message = client.recv(1024) # recv() is a blocking function; will wait until a byte is recvd
            broadcast(message)
        except:
            # get index of client
            index = clients.index(client)

            # remove client from array
            clients.remove(client)

            # close client's connection
            client.close()

            # get client's name using index
            nickname = nicknames[index]
            
            # broadcast leave of client
            broadcast(f"{nickname} has left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break

# constantly receives new connections and do the housekeeping
def receive():
    while True:
        client, address = server.accept()
        print("New connection with {}".format(str(address)))

        # request and store nickname of new client

        # 'NICK' is like a 'reserved' keyword that tells the client program "Give me the nickname"
        client.send('NICK'.encode('ascii')) 
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # print and broadcats nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} has joined!".format(nickname).encode('ascii'))
        client.send("You are connected to server!".encode('ascii'))

        # start thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()