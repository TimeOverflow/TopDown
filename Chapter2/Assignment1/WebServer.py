from socket import *
import time

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12345
serverSocket.bind(('127.0.0.1', serverPort))

serverSocket.listen(2)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(65536).decode()

        filename = message.split()[1][1:] # filename = "HelloWorld.html"
        f = open(filename)
        outputData = f.read()

        responseHeader = ""
        responseHeader +="HTTP/1.1 200 OK\n"
        responseHeader += "Connection: close\n"
        responseHeader += "Date: {}\n".format(time.asctime(time.localtime(time.time())))
        responseHeader += "Server: hahahaha\n"
        responseHeader += "Last-Modified: {}\n".format(time.asctime(time.localtime(time.time())))
        responseHeader += "Content-Length: {}\n".format(len(outputData))
        responseHeader += "Content-Type: text/html\n\n"
        # 这里必须两个\n，因为header与entity body之间要有个换行符

        for header in responseHeader:
            connectionSocket.send(header.encode())

        for i in range(len(outputData)):
            connectionSocket.send(outputData[i].encode())

        connectionSocket.close()

    except IOError:
        responseHeader = "HTTP/1.1 404 Not Found\nConnection: close\n\n"
        connectionSocket.send(responseHeader.encode())
        connectionSocket.close()
