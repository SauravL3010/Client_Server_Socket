import sys

lol = sys.argv[1]
FORMAT = "utf-8"


print(sys.argv)
print(lol.encode(FORMAT))
print(lol.encode(FORMAT).decode(FORMAT))

import socket
sock = socket.socket()
sock.bind(('', 0))
get = sock.getsockname()[1]
print(get)