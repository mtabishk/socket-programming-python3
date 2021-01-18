import socket
s = socket.socket()

server_ip = "192.168.99.101"
server_port = 2222

s.connect( (server_ip, server_port))

while True:
    data = input("<Me>:  ")
    s.send(data.encode() )
    
    msg = s.recv(1024)
    if msg.decode() is not None:
        print(f"{server_ip}:  " + msg.decode() )
