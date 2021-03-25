import time
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for sequence_number in range(1, 10+1):
    message = "Ping " + str(sequence_number) + " " + str(time.asctime(time.localtime(time.time())))
    try:
        send_time = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(65536)
        rtt = time.time() - send_time # 在本机操作Round Trip Time实际上很小的
        print("{}  RTT: {} us".format(modifiedMessage.decode(), rtt * 1000 * 1000))
    except timeout:
        print(message + " timeout")
    pass

clientSocket.close()