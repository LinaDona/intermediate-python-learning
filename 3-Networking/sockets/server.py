'''
- Sockets are a low level communication "mechanism".
- In a communication, two sockets, aka: com endpoints, are used.
- Sockets may be used to communicate across processes on the same computer, on the same local network, or
across the internet.
- A socket can be a UNIX socket or an INTERNET socket. The protocol can be TCP or UDP.
- UDP is used for online gaming or video calls, whereas TCP is used when reliable com is needed.
'''

import socket

# host and port values
host = '127.0.0.1'
port = 55555

# SOCK_STREAM for TCP, SOCK_DGRAM for UDP, AF_INET for IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# where does our socket (server) run? ==> local host on port 55555 (passed as tuple to the bind method)
s.bind((host, port))

# listen for clients
s.listen()

while True:
    client, address = s.accept() 
    print(f"Connected to {address}.")
    # print(f"Client socket: {client.getsockname()}")
    client.send("You are connected!".encode()) # encode in utf-8
    client.close() # close connection when finished

'''
Note that the printed address of the client will have a port different than 55555. Because the latter
is the server's port number while the random-looking number is the client's port number.
'''


