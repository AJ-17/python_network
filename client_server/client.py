import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
host,port='0.0.0.0',9292
client.connect((host,port))
print("Please press enter after recieveing every message!!")

def send():
    while True:
        i = input('You : ');
        client.send(i.encode('utf-8'));

def rec():
    while True:
        m=client.recv(1024).decode('utf-8');
        print(f'\nServer : {m}\nYou : ',end='')
threading.Thread(target=send).start();
threading.Thread(target=rec).start();
