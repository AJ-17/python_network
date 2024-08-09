import socket
import threading
alias=input("Enter the alias : ");

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
ip="0.tcp.in.ngrok.io";
port=14157;
client.connect((ip,port))
print('connected')
def recieve():
    while True:
        m=client.recv(1024).decode('utf-8');
        if m=='alias?':
            client.send(alias.encode('utf-8'))
        else:
            print(m);

def send():
    while True:
        message=f'{alias} : {input("")}'
        client.send(message.encode('utf-8'));

threading.Thread(target=recieve).start();
threading.Thread(target=send).start();
