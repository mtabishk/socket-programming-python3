# import colorama module
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# import pyfiglet module 
from pyfiglet import Figlet, figlet_format
from termcolor import colored

# Heading
print((colored(figlet_format("chatMe  server"), color="red")))

# Body
import threading
import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = ""
port = 2222

s.bind( (host,port))
s.listen()

list_of_conn = []
list_of_colors = ['RED', 'CYAN']


def server_func(csession, addr):
    msg = csession.recv(1024)
    if addr[0] == list_of_conn[0]:
        print(f"{Back.GREEN} Client - {addr[0]} : ", end='\t')
        if msg.decode() is not None:
            print(msg.decode() )
    else:
        print(f"{Back.CYAN} Client - {addr[0]} : ", end='\t')
        if msg.decode() is not None:
            print(msg.decode() )
   
    print(f"{Back.RED} Server - :", end="")
    data = input()
    csession.send(data.encode() )


while True:
    csession, addr = s.accept()
    list_of_conn.append(addr[0])
    t1 = threading.Thread(target=server_func, args=(csession, addr))
    t1.start()

