import socket

# For using UDP (User Datagram) Protocol
ptl = socket.SOCK_DGRAM

# Network Address Family (AF) : INET is for IPv4
naf = socket.AF_INET

# socket object
s = socket.socket(ptl, naf)

#host = socket.gethostname() # for using local machine as host
host = "192.168.1.28"
port = 1234

# binding host and port with the socket object
s.bind( (host,port) )

# recvfrom() method is used to recieve data from UDP Protocol
data = s.recvfrom(1024) # 1024 is size in bytes of data to recieve from the client

print(data)


