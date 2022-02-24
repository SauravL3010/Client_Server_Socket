import sys
from socket import *



# Creating a TCP socket
serverSocket= socket(AF_INET,SOCK_STREAM)

# Binding to a free port and printing it to the screen

serverSocket.bind(('',0))
serverPort= serverSocket.getsockname()[1]
print("SERVER_PORT=" + str(serverPort))
serverSocket.listen(1)

while True:    
    
    # Waiting for a connection request on n_port
    connectionSocket, addr= serverSocket.accept()
    reqCode = connectionSocket.recv(1024).decode()
    
    # Checking if the req_code matches
    if sys.argv[2] == reqCode:

        # Creating a UDP socket and sending the r_port through TCP connection
        s = socket(AF_INET,SOCK_DGRAM)
        s.bind(('',0))
        rPort= s.getsockname()[1]
        connectionSocket.send(str(rPort).encode())
        while True:

            # Receiving input string through UDP connection and sending the modified input to client
            message, clientAddress = s.recvfrom(1024)
            modifiedMessage = message.decode()[::-1]
            s.sendto(modifiedMessage.encode(),clientAddress)
            break
    connectionSocket.close()






