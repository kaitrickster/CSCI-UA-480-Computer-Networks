import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem")

bindsocket = socket.socket()
bindsocket.bind(("127.0.0.1", 10023))
bindsocket.listen()

newsocket, fromaddr = bindsocket.accept()
connstream = context.wrap_socket(newsocket, server_side=True)
data = connstream.recv(1024)
print(data.decode())
