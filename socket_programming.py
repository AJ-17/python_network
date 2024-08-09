# Socket programming in python 
'''
Socket programming is a way of connection between two nodes or two sockets to communicate with each other

Server socket listen on port at IP and client socket connects to server

'''

import socket 
import sys
try: 
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket connection succesfull");
except socket.error as error:
    print(f'Socket creation failed with error {error}') 
    
# here we have two paramters so the first one is 'socket.AF_INET' which represent a ipv4  and the second parameter represent the Tcp protocoal
try: 
    ip = socket.gethostbyname('www.github.com');
except socket.gaierror as error:
    print(f'error resolving the host')
    sys.exit();
port=80;
print(ip)
s.connect((ip,port))
print(f'Socket has succesfully connected to github on port == {ip}:{port}')


































