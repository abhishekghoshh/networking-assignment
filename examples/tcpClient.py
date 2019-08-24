#sample tcp client 

import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("127.0.0.1",4444))
data= mysocket.recv(2048)
for i in range(1,9):
    print data
    mysocket.send("I am from client")
mysocket.close();

