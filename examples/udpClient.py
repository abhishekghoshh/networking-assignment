#simple udp client

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysock.connect(('127.0.0.1',1337))

mysock.sendto("hello from client ",('127.0.0.1',1337))
data=mysock.recvfrom(2048)
print data

mysock.close