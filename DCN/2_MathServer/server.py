import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    a, address = sock.recvfrom(4096)
    b, address = sock.recvfrom(4096)
    c, address = sock.recvfrom(4096)
    a=int(a)
    b=int(b)
    if c =='0':
    	result = str(a+b)
    elif c =='1':
    	result = str(a-b)
    elif c =='2':
    	result = str(a*b)
    elif c =='3':
    	result = str(a/b)
    elif c =='4':
    	result = str(a%b)
    
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, result
    
    if c:
        sent = sock.sendto(result, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
