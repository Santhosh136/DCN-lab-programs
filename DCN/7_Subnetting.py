ip=input("enter the ip address")
p=ip[:-1]
s=int(input("enter the subnet mask"))
net=s%24
netno=pow(2,net)
host=8-net
hostno=pow(2,host)
print("no of hosts",hostno-2)
count=0
for i in range(1,netno+1):
        print("network ",i,"address-->",p,count,end="\n")
        print("start-->",p,count+1,end="\n")
        print("end--->",p,count+hostno-2,end="\n")
        print(end="\n")
        count=count+hostno

