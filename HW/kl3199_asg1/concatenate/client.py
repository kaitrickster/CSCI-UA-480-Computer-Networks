import sys
import os
import random
import string
# TODO: Import socket library
from socket import *

# Random alphanumeric string of length l
def rand_str(l):
  ret = ''
  for i in range(l):
    ret += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
  return ret

NUM_TRANSMISSIONS=10
if (len(sys.argv) < 2):
  print("Usage: python3 "  + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port=int(sys.argv[1])

# TODO: Create a socket for the client
tcp_client = socket(AF_INET, SOCK_STREAM)

# TODO: Connect this socket to the server
tcp_client.connect(("127.0.0.1", server_port))

# Transmit NUM_TRANSMISSIONS number of times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Generate a random string of length 10 using rand_str function
  rand_string = rand_str(10)

  # TODO: Send random string to the server
  tcp_client.send(rand_string.encode())

  # TODO: Print data for debugging
  print("sent:", rand_string)

  # TODO: Receive concatenated data back from server as a byte array
  recv_data = tcp_client.recv(256)

  # TODO: Print out concatenated data for debugging
  print("received:", recv_data.decode(), "\n")
  
# TODO: close socket
tcp_client.close()
