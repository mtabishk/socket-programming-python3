import socket
import threading
import subprocess as sp


# For using UDP (User Datagram) Protocol
ptl = socket.SOCK_DGRAM

# Network Address Family (AF) : INET is for IPv4
naf = socket.AF_INET

# socket object
s = socket.socket(ptl, naf)

#host = socket.gethostname() # for using local machine as host
host = "192.168.1.28"
port = 1234
def recieve():
    # binding host and port with the socket object
    s.bind( (host,port) )
    
    while True:
        data = s.recvfrom(1024) # 1024 is size in bytes of data to recieve from the client

        msg = data[0].decode()
        client = data[1][0]
        print("Client: {0} \tmessage: {1}".format(client , msg) )

def send():
    while True:
        local_ip = sp.getoutput("ip -4 addr show enp0s3 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")
        msg = input("Me@"+local_ip+": ")
        s.sendto( msg.encode() , ("192.168.1.33",4321)  )


# 2 threads: one for recieving message and one for sending 'em
t1 = threading.Thread(target = send)
t2 = threading.Thread(target = recieve)

# recvfrom() method is used to recieve data from UDP Protocol
t1.start()
t2.start()
