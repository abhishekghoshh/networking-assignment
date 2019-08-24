#sample tcp server

import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1",4444))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()
for i in range(1,9):
    client.send("knock knock knock, I am server")
    data=client.recv(2048)
    print data
mysocket.close()
