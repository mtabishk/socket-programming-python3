import socket
import subprocess as sp
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recieve():
    host = "192.168.1.28"
    port = 1234
    s.bind( (host,port) )
    while True:
        # recieve message from server
        data = s.recvfrom(1024)
        rec_msg = data[0].decode()
        server = data[1][0]
        print("Server: {0} \tmessage: {1}".format(server , rec_msg) )

def send():
    msg = "start"
    while msg != "end":
        local_ip = sp.getoutput("ip -4 addr show enp0s3 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")
        msg = input("Me@"+local_ip+": ")
        s.sendto( msg.encode() , ("192.168.1.28",1234)  )

t1 = threading.Thread(target = recieve)
t2 = threading.Thread(target = send)

t1.start()
t2.start()


