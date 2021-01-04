import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.28"
port = 1234

s.bind( (host,port) )

s.listen()
conn, addr = s.accept()

while True:
    #conn, addr = s.accept()
    msg = conn.recv(1024)
    if msg.decode() is not None:
        print(str(addr[0]) + ":  " + msg.decode() )
    data = input("<Server> :  ")
    conn.send(data.encode() )



