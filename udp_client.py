import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello Tabish"
s.sendto( msg.encode() , ("192.168.1.28",1234)  )