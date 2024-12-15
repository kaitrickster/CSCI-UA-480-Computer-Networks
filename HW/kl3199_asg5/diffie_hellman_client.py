from socket import *
import random

p = 23
g = 5

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 2525))

a = random.randint(1, 10)
A = (g ** a) % p

client.send(str(A).encode())
recv_data = client.recv(256)

B = int(recv_data.decode())
s = (B ** a) % p

print(s)
