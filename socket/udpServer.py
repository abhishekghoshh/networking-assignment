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


mysocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysocket.bind(('127.0.0.1',1337))

clientdata,addr=mysocket.recvfrom(2048)
print clientdata

print "address of the client is ",addr
mysocket.sendto("hello from server ",addr)

localtime,addr=mysocket.recvfrom(2048)
hr= int(localtime[11:13])
mysocket.sendto(greeting(hr),addr)

while True:
    option,addr=mysocket.recvfrom(2048)
    op=int(option)
    if(op==5):
        break
    else:
        num,addr=mysocket.recvfrom(2048)
        num1=float(num)
        mysocket.sendto("num 1 has received",addr)
        num,addr=mysocket.recvfrom(2048)
        num2=float(num)
        
    mysocket.sendto(math(op,num1,num2),addr)

mysocket.close()