import socket

hostname = 'localhost'
addr = socket.gethostbyname(hostname)

print("{}: {}".format(hostname, addr))

