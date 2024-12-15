import sys
# TODO: import socket libraries
from socket import *


NUM_TRANSMISSIONS=200
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections
relay_socket = socket(AF_INET, SOCK_STREAM)

# TODO: Bind the relay's socket to relay_port
relay_socket.bind(("127.0.0.1", relay_port))

# TODO: Put relay's socket in LISTEN mode
relay_socket.listen()

# TODO: Accept a connection first from sender.py (accept1)
comm_socket_sender, sender_addr = relay_socket.accept()

# TODO: Then, accept a connection from receiver.py (accept2)
comm_socket_receiver, receiver_addr = relay_socket.accept()

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive data from sender socket (the return value of accept1)
  # Be careful with the length of data you receive
  raw_data = comm_socket_sender.recv(200)
  
  # TODO: Check for any bad words and replace them with the good words
  # Replace 'virus' with 'groot'
  # Replace 'worm' with 'hulk'
  # Replace 'malware' with 'ironman'
  raw_data_str = raw_data.decode()
  processed_str = raw_data_str.replace("virus", "groot")
  processed_str = processed_str.replace("worm", "hulk")
  processed_str = processed_str.replace("malware", "ironman")

  # TODO: and forward the new string to the receiver socket (the return value of accept2)
  comm_socket_receiver.send(processed_str.encode())
  
  # TODO: print data that was relayed
  print("relayed: \n" + processed_str + "\n")

# TODO: Close all open sockets
comm_socket_sender.close()
comm_socket_receiver.close()
relay_socket.close()
