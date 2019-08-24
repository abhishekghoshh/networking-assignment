#sample tcp client 

import socket
import time

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("127.0.0.1",4444))

data= mysocket.recv(2048)
print(str(data))
mysocket.send("I am from client".encode())

localtime = time.asctime(time.localtime(time.time()))
mysocket.send(localtime.encode())
greeting= mysocket.recv(2048)
print((greeting))

while True:
    print("Choose from the option below")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")
    
    op=int(input("Enter your option from 1 to 5 : "))
    mysocket.send(str(op).encode())
    if(op==5):
        break
    else:
        num1=float(input("Enter number one : "))
        mysocket.send(str(num1).encode())
        num2=float(input("Enter number one : "))
        mysocket.send(str(num2).encode())
    result=mysocket.recv(2048)
    print(result)
    print("\n\n\n")

print("connection is closed")
mysocket.close();

