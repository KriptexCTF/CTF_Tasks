import sys
from socket import socket
import base64
arg = (sys.argv[1]).split(':')

sock = socket()
sock.connect((arg[0], int(arg[1])))
print((sock.recv(1024)).decode("ascii"))
#print((sock.recv(1024)).decode("ascii"))

for i in range(104):
	a = ((sock.recv(1024)).decode("utf-8"))
	((sock.recv(1024)).decode("ascii"))
	print(a)
	a = a.encode("utf-8")
	b = base64.b64decode(a)
	c = b.decode("ascii")
	print('|' + c + '|')
	sock.send(str.encode(c + '\n'))
	print((sock.recv(1024)).decode("ascii"))
print(a)
