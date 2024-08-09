'''

SOCKETS 

 They are just communication endpoints
 It don't need to be a internet socket
 They can be sockets for OS ,bluetooth socket etc
  
 eg :- socket.AF_INET means internet socket for IPV4
       socket.AF_INET6 means internet socket for IPV6
       socket.AF_BLUETOOTH means bluetooth socket


       socket.SOCK_STREAM   for TCP
       socket.SOCK_DGRAM    for UDP

'''
import socket
import sys
host=socket.gethostbyname(socket.gethostname())
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # now these is a socket but we don't know why the socket will be used for 

HOST='127.0.0.1'
port=9191

print(host)

server.bind((HOST,port))
server.listen(5)
# 5 means that how many connection we allow without reject the new one
while True:
      communication_socket,address=server.accept()
      print(f"Connected to {address}")
      message=communication_socket.recv(1024).decode('utf-8')
      print(f"Message from client is  : {message}")
      communication_socket.send("Got the message".encode('utf-8'))

















