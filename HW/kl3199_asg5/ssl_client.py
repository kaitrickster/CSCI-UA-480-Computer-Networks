import socket
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="127.0.0.1")
conn.connect(("127.0.0.1", 10023))
cert = conn.getpeercert()
conn.sendall(b"Hello")
