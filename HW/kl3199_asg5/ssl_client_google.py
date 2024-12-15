import pprint
import socket
import ssl

context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="www.google.com")
conn.connect(("www.google.com", 443))
cert = conn.getpeercert()
conn.sendall(b"GET /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
pprint.pprint(conn.recv(1024).split(b"\r\n"))

print("\n\n---------------tuning receive bytes--------------\n")

conn5 = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="www.google.com")
conn5.connect(("www.google.com", 443))
cert5 = conn5.getpeercert()
conn5.sendall(b"GET /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
pprint.pprint(conn5.recv(4096).split(b"\r\n"))

print("\n\n\n---------------printing out certificates--------------\n")
pprint.pprint(cert)
