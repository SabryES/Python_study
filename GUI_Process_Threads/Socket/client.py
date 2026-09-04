import socket 
import time

# 1_create socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM )#ipv4 , TCP


client.connect(('localhost',12345))

while True :
    message = "[Client] How are you "
    client.send(message.encode('utf-8'))
    message=client.recv(1024)
    print(f"i am client and Received message:{message.decode('utf-8')}")
    
    # client.close()
    time.sleep(1)