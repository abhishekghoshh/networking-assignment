#sample tcp server

import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1",4444))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()

client.send(("knock knock knock, I am server, your connected port no is "+ str(port)).encode('utf8'))
data=client.recv(2048)
print ((data).decode("utf-8"))
print("\n\n\n")

while True:
    mssg=input("Server : ")
    client.send(mssg.encode('utf8'))
    data=client.recv(2048)
    print (("Client :",data).decode("utf-8"))

mysocket.close()
