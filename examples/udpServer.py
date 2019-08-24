#simple udp server

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysock.bind(('127.0.0.1',1337))

clientdata,addr=mysock.recvfrom(2048)
print clientdata

print "address of the client is ",addr
mysock.sendto("hello from server ",addr)

mysock.close()