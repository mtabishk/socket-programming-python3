import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("192.168.1.28", 1234) )

while True:
    data = input("<Me>:  ")
    s.send(data.encode() )
    
    msg = s.recv(1024)
    if msg.decode() is not None:
        print("192.168.1.28:  " + msg.decode() )

