# TODO: import socket library
from socket import *
import sys
import random
NUM_TRANSMISSIONS=10
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port=int(sys.argv[1])

# TODO: Create a datagram socket for the client
client = socket(AF_INET, SOCK_DGRAM)

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # Create an RPC request to compute if a number is prime
  rpc_data="prime(" + str(random.randint(0, 100)) + ")"

  # TODO: Send RPC request (i.e., rpc_data) to the server
  client.sendto(rpc_data.encode(), ("127.0.0.1", server_port))

  # Print debugging information
  print("sent: " + rpc_data);

  # TODO: Receive result back from the server into the variable result_data
  result_data = client.recv(128)

  # TODO: Display it in the format "prime: yes" or "prime: no"
  print("prime:", result_data.decode(), "\n")

# TODO: Close any sockets that are open
client.close()
