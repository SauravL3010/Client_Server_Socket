import socket 
import sys

SERVER_ADDRESS = sys.argv[1]
N_PORT = int(sys.argv[2])
REQ_CODE = int(sys.argv[3])
CLIENT_STRING = sys.argv[4]

HEADER = 1024
FORMAT = 'utf-8' 
ADDR = (SERVER_ADDRESS, N_PORT)

# Creating TCP connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) # throws an unhandled error if n_port is incorrect 

def send():
    
    # Sending req_code to server
    encoded_req_code = str(REQ_CODE).encode(FORMAT)
    client.send(encoded_req_code)
    
    # receiving r_port from server
    random_port = int(client.recv(HEADER).decode(FORMAT)) # NOTE: if req_code sent is invalid, this line throws an unhandled error and seizes to connect

    client.close() # close connection at N_PORT

    # Creating UDP connection and sending the input string
    NEW_ADDR = (SERVER_ADDRESS, random_port)
    new_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client.connect(NEW_ADDR)
    encoded_client_string = CLIENT_STRING.encode(FORMAT)
    new_client.send(encoded_client_string)

    # receiving the reversed string from server and printing it out to the console
    reversed_string = new_client.recv(HEADER).decode(FORMAT)
    new_client.close() # close connection at r_port
    print(reversed_string)

send()

