import socket
def localHostInfo():
    h=socket.gethostname()
    i=socket.gethostbyname(h)
    print "hostname is ",h
    print "If internet is on then it will show the actuall ip address otherwise it will show the loop back address"
    print "ip address is ",i
    
localHostInfo()

def remoteHostInfo():
    rhost=raw_input("ENter remote hostname : ")
    rip=socket.gethostbyname(rhost)
    try:
        print "IP address of remote host is ",rip
    except socket.error,err_mssg:
        print err_mssg
        
remoteHostInfo()