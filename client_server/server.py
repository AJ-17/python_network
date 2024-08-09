import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
port=9292
server.bind(('0.0.0.0',9292));
server.listen(5);
client,address=server.accept();
print(F'Connected to address  :{address}')
def send():
        while True:
            i=input("You : ");
            client.send(i.encode('utf-8'))

def rec():
        while True:
            m=client.recv(1024).decode('utf-8')
            print(f'\nclient : {m}\nYou : ',end='')

        
threading.Thread(target=send).start();
threading.Thread(target=rec).start();

    

