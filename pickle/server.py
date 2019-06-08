import socket
import time
import datetime
import pickle


HEADERSIZE = 10


mySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is the ipv4 , TCP
mySocket.bind((socket.gethostname(), 1234)) #server should bind

mySocket.listen(5) # wait for a queue of 5

while True:
    clientSocket, address = mySocket.accept()
    print("Connection established with {}".format(address))
    msg = "Welcome to my server you douchebag!"

    msg = {
        1: "Ben",
        2: "Vishal"
    }
    msg = pickle.dumps(msg)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+ msg

    clientSocket.send(msg)

