#sample tcp server

import socket
import time;

def greeting(hr):
    if hr>=5 and hr<12:
        return "Good Morning"
    if hr>=12 and hr<15:
        return "Good Noon"
    if hr>=15 and hr<18:
        return "Good Afternoon"
    if hr>=18 and hr<20:
        return "good Evening"
    if hr>=20 and hr<23:
        return "Good Night"
    if hr>=0 and hr<5:
        return "Good Night"
    
def math(op,num1,num2):
    if(op==1):
        add= float(num1+num2)
        return "The addition is "+str(add)
    if(op==2):
        sub= float(num1-num2)
        return "The substraction is "+str(sub)
    if(op==3):
        mul= float(num1*num2)
        return "The multiplication is "+str(mul)
    if(op==4):
        div= float(num1/num2)
        return "The division is "+str(div)

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1",4444))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()
print(("Ip address and port from which server is connected to is ",ip,port))

client.send("knock knock knock, I am server".encode())
data=client.recv(2048)
print(data)

localtime=client.recv(2048)
hr= int(localtime[11:13])
client.send(greeting(hr).encode())

while True:
    op=int(client.recv(2048))
    if(op==5):
        break
    else:
        num1=float(client.recv(2048))
        num2=float(client.recv(2048))
    client.send(math(op,num1,num2).encode())
    print("\n\n\n")
    
print("connection is closed")
mysocket.close()
