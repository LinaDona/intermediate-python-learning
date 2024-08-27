import socket
import threading

host = '127.0.0.1'
port = 55555
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# listening to the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print("An error has occured!")
            client.close()
            break

def write():
    while True:
        message = "{}: {}".format(nickname, input(""))
        client.send(message.encode('ascii'))

receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()

