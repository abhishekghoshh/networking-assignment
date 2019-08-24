#sample tcp client 

import socket
import time

mysocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',1337)
mysocket.connect(addr)

mysocket.sendto("hello from client ",addr)
data=mysocket.recvfrom(2048)
print data

localtime = time.asctime(time.localtime(time.time()))
mysocket.sendto(localtime,addr)
greeting= mysocket.recv(2048)
print greeting

while True:
    print "Choose from the option below"
    print "1.Addition"
    print "2.Substraction"
    print "3.Multiplication"
    print "4.Divison"
    print "5.Exit"
    
    op=int(raw_input("Enter your option from 1 to 5 : "))
    mysocket.sendto(str(op),addr)
    if(op==5):
        break
    else:
        num1=float(raw_input("Enter number one : "))
        mysocket.sendto(str(num1),addr)
        num2=float(raw_input("Enter number one : "))
        mysocket.sendto(str(num2),addr)
    fau=mysocket.recvfrom(2048)
    result=mysocket.recvfrom(2048)
    print result

print "connection is closed"

mysocket.close