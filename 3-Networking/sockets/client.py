import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
message = s.recv(1024) # receive 1024 bytes

print(f"Connecting attempt from {s.getsockname()}")
print(f"Connecting to {s.getpeername()}")
print("............")
print(message.decode())

s.close()