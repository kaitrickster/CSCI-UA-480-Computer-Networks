from socket import *
import random

p = 23
g = 5

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 2525))

b = random.randint(1, 10)
B = (g ** b) % p

server.listen()
(comm_socket, client_addr) = server.accept()
recv_data = comm_socket.recv(256)

comm_socket.send(str(B).encode())

A = int(recv_data.decode())
s = (A ** b) % p

print(s)
