import pprint
import socket
import ssl

context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="www.nytimes.com")
conn.connect(("www.nytimes.com", 443))
cert = conn.getpeercert()
conn.sendall(b"GET /index.html HTTP/1.1\r\nHost: www.nytimes.com\r\n\r\n")
pprint.pprint(conn.recv(1024).split(b"\r\n"))

print("\n\n---------------printing out certificates--------------\n")
pprint.pprint(cert)
