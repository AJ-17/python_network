import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
HOST='127.0.0.1'
port=9191
client.connect((HOST,port))
client.send("Hello world".encode('utf-8'))
print(client.recv(1024).decode('utf-8'));





# to conform if a port is not already in use use the commad in terminal netstat