import socket
import time

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = 'H'
    i=0
    s=0
    while i<1000:
        t1=time.time()
        for j in range(2048):
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(2*1024).decode()  # receive response
        t2=time.time()
        print(str(i)+')'+'Received from server: ' + data)  # show in terminal
        t=t2-t1
        s=s+t
        i=i+1
        #message = input(" -> ")  # again take input
    avg=s/1000
    print("The Rotational Latency:"+str(avg))
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()


