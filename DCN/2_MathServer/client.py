import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'


print("\nEnter two numbers:")
a= str(input())
b= str(input())
print("Enter operation:")
print("Enter 0 for addition \n1 for difference\n2 for Multiplication\n3 for Division\n4 for modulus")
c= str(input())



# Send data
print >>sys.stderr, 'sending "%s"' % message
#sent = sock.sendto(message, server_address)
sent1 = sock.sendto(a, server_address)
sent2 = sock.sendto(b, server_address)
sent3 = sock.sendto(c, server_address)
# Receive response
print >>sys.stderr, 'waiting to receive'
data, server = sock.recvfrom(4096)
print >>sys.stderr, 'received "%s"' % data

print >>sys.stderr, 'closing socket'
sock.close()
