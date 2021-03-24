from socket import *
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('server_host', type=str, help='server ip')
parser.add_argument('server_port', type=int, help='server port')
parser.add_argument('filename', type=str, help='file name')
args = parser.parse_args()

serverName = args.server_host
serverPort = args.server_port
filename = args.filename

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = ""
message += "GET " + filename + " HTTP/1.1\n"  # filename的格式为/HelloWorld.html
message += "Host: " + serverName + "\n"
message += "Connection: close\n\n"
clientSocket.sendto(message.encode(), (serverName, serverPort))

response = ""

# 用while循环接收，因为服务器发送是一个字符一个字符发送的
while True:
    recvMessage, serverAddress = clientSocket.recvfrom(65536)
    if not recvMessage:
        break
    response += recvMessage.decode()


print(response)

clientSocket.close()
