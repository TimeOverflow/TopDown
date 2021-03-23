from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(2)
print("The server is ready to receive...")

while True:
    ConnectionSocket, addr = serverSocket.accept()
    sentence = ConnectionSocket.recv(2048).decode()
    capitalizedSentence = sentence.upper()
    ConnectionSocket.send(capitalizedSentence.encode())
    ConnectionSocket.close()