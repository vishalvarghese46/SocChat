import socket

HEADERSIZE = 10

mySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((socket.gethostname(), 1234)) # client should connect to it


while True:
    full_msg = ''
    new_msg = True
    while True:
            msg = mySocket.recv(16)
            if new_msg:
                print(f'Length of new_msg {msg[:HEADERSIZE]}')
                msglen = int(msg[:HEADERSIZE])
                new_msg = False
            print(f"full message length: {msglen}")
            full_msg += msg.decode("utf-8")
            print(len(full_msg))

            if(len(full_msg)-HEADERSIZE) == msglen:
                print("Full message recvd mowne!")
                print(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = ''


