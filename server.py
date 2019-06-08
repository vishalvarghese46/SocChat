import socket
import time
import datetime

HEADERSIZE = 10


mySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is the ipv4 , TCP
mySocket.bind((socket.gethostname(), 1234)) #server should bind

mySocket.listen(5) # wait for a queue of 5

while True:
    clientSocket, address = mySocket.accept()
    print("Connection established with {}".format(address))
    msg = "Welcome to my server you douchebag!"
    msg = f'{len(msg):<{HEADERSIZE}}'+ msg

    clientSocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f'The time is: {datetime.datetime.now()}'
        msg = f'{len(msg):< {HEADERSIZE}}'+ msg
        print(str(msg))
        clientSocket.send(bytes(str(msg), "utf-8"))

