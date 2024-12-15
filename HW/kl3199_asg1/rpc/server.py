#TODO: import socket library
from socket import *
import sys
NUM_TRANSMISSIONS=10
if(len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
server = socket(AF_INET, SOCK_DGRAM)

# TODO: Bind it to server_port
server.bind(("127.0.0.1", server_port))

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive RPC request from client
  recv_data, client_addr = server.recvfrom(128)

  # TODO: Turn byte array that you received from client into a string variable called rpc_data
  rpc_data = recv_data.decode()

  # TODO: Parse rpc_data to get the argument to the RPC.
  # Remember that the RPC request string is of the form prime(NUMBER)
  number_str = rpc_data[6:len(rpc_data)-1]

  # TODO: Print out the argument for debugging
  print("argument is", number_str)

  # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
  number = int(number_str)
  primality = "yes"
  if number == 0 or number == 1:
    primality = "no"
  elif number >= 3:
    for i in range(2, number):
      if number % i == 0:
        primality = "no"
        break

  # TODO: Send the result of primality check back to the client who sent the RPC request
  server.sendto(primality.encode(), client_addr)

# TODO: Close server's socket
server.close()
