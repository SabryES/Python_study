import socket 
import time
# 1_create socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM )#ipv4 , TCP
s.bind(('localhost',12345)) #bind to local host on port 12345
s.listen(5) #listen for 5 incoming connections ya3ny law 5 connection at same time ana 2a2dar 2asta2belha 
print("server is listening on port 12345...")
cliet_scocket,addr=s.accept()
while True :
    print(f"connection from {addr}")
    message=cliet_scocket.recv(1024)
    print(f"iam [server] and Received message :{message.decode('utf-8')} ")
    message = "[server ] hello, clieent"
    cliet_scocket.send(message.encode())
    # cliet_scocket.close()
    time.sleep(1)