import socket
import threading

def client(number):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1", 55555))
    message = clientSocket.recv(1024).decode()
    print(f"Client {number}: "+message)

    clientSocket.close()

t1 = threading.Thread(target=client, args=(1,))
t2 = threading.Thread(target=client, args=(2,))

t1.start()
t2.start()


