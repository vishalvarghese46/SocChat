import socket
import select

HEADERSIZE = 10

IP = "192.168.1.142"
PORT = "1234"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind((IP, PORT))
serverSocket.listen()

socketList = [serverSocket]

clients = {} #client sockets will be the key and user data will be the value


def receiveMessage(clientSocket):
    try:
        messageHeader = clientSocket.recv(HEADERSIZE)
        if not len(messageHeader):
            return False

        messageLenth = int(HEADERSIZE.deoode("utf-8"))
        return {"header": messageHeader, "data": clientSocket.recv(messageLenth)}

    except:
        return False

whi