import sys
from socket import *



serverAddress= sys.argv[1]
serverPort= int(sys.argv[2])

# Creating TCP connection and sending req_code
clientSocket= socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress,serverPort))
n_port=sys.argv[3]
clientSocket.send(n_port.encode()) 

# Receiving r_port from server and closing the TCP connection
rPort= int(clientSocket.recv(1024).decode())
clientSocket.close()

# Creating UDP connection and sending the input string
c= socket(AF_INET, SOCK_DGRAM)
c.sendto(sys.argv[4].encode(),(serverAddress,   rPort))

# Recieving the result string from server, printing it and closing the UDP connection
modifiedMessage, serverAddress= c.recvfrom(1024)
print (modifiedMessage.decode())
c.close()