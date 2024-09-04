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
Notice that we are always encoding and decoding the messages here. The reason for this is that we 
can only send bytes and not strings. So we always need to encode messages (for example using ASCII), 
when we send them and decode them, when we receive them.
'''

def kick_user(nickname):
    if nickname in nicknames:
        index = nicknames.index(nickname)
        kicked_client = clients[index]
        kicked_client.send("You were kicked by an admin.".encode('ascii'))
        if kicked_client in clients:
            clients.remove(kicked_client)
        nicknames.remove(nickname)
        kicked_client.close()
        broadcast(f"{nickname} was kicked by an admin".encode('ascii'))

def handle_client(client):
    # get index of client
    client_index = clients.index(client)

    # get client's name using index
    nickname = nicknames[client_index]

    while True:
        try:
            msg = message = client.recv(1024) # recv() is a blocking function; will wait until a byte is recvd
            message = message.decode('ascii')
            if message:
                if message[len(nickname)-1+3] == '/':
                    if nickname == "admin":
                        words = message.split()
                        # kicking a chat member
                        if words[1] == "/kick":
                            kick_user(words[2])

                        elif words[1] == "/ban":
                            pass

                        else:
                            client.send("Not a valid command.".encode('ascii'))
                    else:
                        client.send("Non admin member cannot execute commands.".encode('ascii'))
                else:
                    if client in clients:
                        broadcast(msg)
            # if message is empty
            else:
                client.close()
                break
        except:
            # remove client from array
            if client in clients:
                clients.remove(client)

            if client.fileno() != -1:
                # close client's connection
                client.close()
                # broadcast leave of client
                broadcast(f"{nickname} has left the chat!".encode('ascii'))

            # remove nickname from array
            if nickname in nicknames:
                nicknames.remove(nickname)
            break


# constantly receives new connections and do the housekeeping
def receive():
    while True:
        client, address = server.accept()
        print("New connection with {}".format(str(address)))

        # request and store nickname of new client
        # 'NICK' is like a 'reserved' keyword that tells the client program "Give me the nickname"
        client.send("NICK".encode('ascii')) 
        nickname = client.recv(1024).decode('ascii')

        if nickname == "admin":
            client.send("ADMINPASS".encode('ascii'))
            pw = client.recv(1024).decode('utf-8')
            if len(pw) <= 0:
                print("didn't recv anything")
                client.close()
                continue
            if pw == "pw":
                client.send("You are in, mr ADMIN".encode('ascii'))
            else:
                client.send("Password for ADMIN is wrong!".encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        # print and broadcast nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} has joined!".format(nickname).encode('ascii'))
        client.send("You are connected to server!".encode('ascii'))

        # start thread for client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()