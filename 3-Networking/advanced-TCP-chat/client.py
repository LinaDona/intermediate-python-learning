import socket
import threading
import time

host = '127.0.0.1'
port = 55555
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

lock = threading.Lock()

# listening to the server
def receive():
    lock.acquire()
    if nickname == "admin":
        for i in range(2):
            message = client.recv(1024).decode('ascii')
            if message == 'ADMINPASS':
                msg = "{}".format(input("Enter password for admin: "))
                msg = msg.encode('utf-8')
                client.send(msg)
            elif message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
    lock.release()
    
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message:
                if message == 'NICK':
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            else:
                # If message is empty, the server has closed the connection
                print("Connection closed by the server.")
                client.close()
                break
        except Exception as e:
            print(f"An error has occured: {e}")
            client.close()
            break

def write():
    time.sleep(1)
    while True:
            try:
                message = "{}: {}".format(nickname, input(""))
                client.send(message.encode('ascii'))

            except BrokenPipeError:
                print("Cannot send message. Connection broken.")
                client.close()
                break
    
            except:
                print("An error occured while sending messages.")
                break

receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()




















'''
import socket
import threading

host = '127.0.0.1'
port = 55555
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

lock = threading.Lock()

# listening to the server
def receive():
    global lock
    while True:
        try:
            lock.acquire()
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                
                client.send(nickname.encode('ascii'))
                
            elif message == 'ADMINPASS':
                
                msg = "{}".format(input("Enter password for admin: "))
                msg = msg.encode('utf-8')
                client.send(msg)
                
            else:
                print(message)
            lock.release()

        except Exception as e:
            print(f"An error has occured: {e}")
            client.close()
            break

def write():
    global lock
    while True:
        try:
            lock.acquire()
            message = "{}: {}".format(nickname, input(""))
            client.send(message.encode('ascii'))
            lock.release()
        except Exception as e:
            print(f"An error occured while sending messages: {e}")
            break

receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()

'''

