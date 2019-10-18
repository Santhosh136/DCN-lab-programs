import random
def main():
    ar=[]
    n=int(input("Enter the Frame size"))
    for i in range(0,n):
        x=int(input("Enter the Frame Element\t"))
        ar.append(x)
    y=int(input("Enter the Window size"))
    ran=random.randint(0,y)
    print("\nWindow Frames\n")
    for i in range(0,y):
        if(i!=ran):
            print("Frame :",ar[i],"received")
            print("Acknowledgement received for Frame",ar[i],"\n")
        else:
            print("Frame :",ar[ran],"not received")
            print("Acknowledgement not received for Frame",ar[ran],"\n")
    number=ran+y
    print("\nWindow Frames\n")
    for i in range(ran,number):
            print("Frame :",ar[i],"revceived")
            print("Acknowledgement received for Frame",ar[i],"\n")
    final=number+y
    print("\nWindow Frames\n")
    for i in range(number,final):
        print("Frame :",ar[i],"received")
        print("Acknoweledgement received for Frame",ar[i],"\n")
    print("\nWindow Frames\n ")
    if(final!=n):
        for i in range(final,n):
            if (i!=(final+y)):
                print("Frame :",ar[i],"received")
                print("Acknoweledgement received for Frame",ar[i],"\n")
            else:
                print("\nWindow Frames\n")
                print("Frame :",ar[i],"received")
                print("Acknoweledgement received for Frame",ar[i],"\n")   
if __name__ == '__main__':
    main()
