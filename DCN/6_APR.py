arp={'10.1.24.48':'10:FF:54:65','10.2.56.98':'10:YY:76:UT'}
#print("The ip address available are,end="\n"")
print("   IP   :   MAC ",end="\n")
for x in arp:
        print(x,':',arp[x],)
print(end="\n")        
y=input("enter the IP address")
print(y,"the mac is",arp[y],end="\n")

z=input("enter the mac")
for x in arp:
        if z==arp[x]:
                print(z,"the ip is",x)
