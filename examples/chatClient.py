#sample tcp client 

import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("127.0.0.1",4444))

data= mysocket.recv(2048)
print ((data).decode("utf-8"))
mysocket.send(("I am from client").encode('utf8'))
print("\n\n\n")

while True:
    msg=mysocket.recv(2048)
    print (("Server :",msg).decode("utf-8"))
    data=input("Client : ")
    mysocket.send(data.encode('utf8'))

mysocket.close();

