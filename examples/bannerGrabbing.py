import socket
#socket.setdefaulttimeout(2)

sock=socket.socket()
ip_addr=raw_input("Please enter targer ip ")
port=int(raw_input("Please enter targer port "))
sock.connect((ip_addr,port))
print sock.recv(1024)
sock.close()