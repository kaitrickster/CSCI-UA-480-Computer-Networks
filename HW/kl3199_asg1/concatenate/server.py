# TODO: import socket library
import sys
import random
import string
from socket import *

# Function to generate random strings of length l
def rand_str(l):
  ret = ''
  for i in range(l):
    ret += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
  return ret

NUM_TRANSMISSIONS=10
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port=int(sys.argv[1])

# TODO: Create a socket for the server on localhost
tcp_server = socket(AF_INET, SOCK_STREAM)

# TODO: Bind it to a specific server port supplied on the command line
tcp_server.bind(("127.0.0.1", server_port))

# TODO: Put server's socket in LISTEN mode
tcp_server.listen()

# TODO: Call accept to wait for a connection
(comm_socket, client_addr) = tcp_server.accept()

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: receive data over the socket returned by the accept() method
  recv_data = comm_socket.recv(256)

  # TODO: print out the received data for debugging
  print("received:", recv_data.decode())

  # TODO: Generate a new string of length 10 using rand_str
  rand_string = rand_str(10)
  print("appended:", rand_string, "\n")

  # TODO: Append the string to the buffer received
  call_back = rand_string.encode() + recv_data

  # TODO: Send the new string back to the client
  comm_socket.send(call_back)

# TODO: Close all sockets that were created
comm_socket.close()
tcp_server.close()
