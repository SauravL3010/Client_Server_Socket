import socket
import sys

N_PORT = int(sys.argv[1])
REQ_CODE = int(sys.argv[2])


HEADER = 1024 
SERVER_ADDRESS = '127.0.0.1'
ADDR = (SERVER_ADDRESS, N_PORT)
FORMAT = 'utf-8'

# Creating a TCP socket at port=N_PORT and local SERVER_ADDRESS
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn):

    # receives req_code from client 
    received_req_code = conn.recv(HEADER).decode(FORMAT)

    # Checkes if req_code matches to establish connection 
    if int(received_req_code) == REQ_CODE:
        # End of negotiation

        # Creating a UDP socket and sending the r_port through TCP connection
        random_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        random_server.bind(('', 0))
        r_port = str(random_server.getsockname()[1]).encode(FORMAT)
        conn.send(r_port)

        random_server.listen()
        while True:
            random_conn, random_addr = random_server.accept()       
            received_client_string = random_conn.recv(HEADER).decode(FORMAT) # receive string from client       
            client_string_to_be_sent = received_client_string[::-1].encode(FORMAT) # reverse string
            random_conn.send(client_string_to_be_sent) # send reversed string to the client 
            random_conn.close() # close connection at r_port
            break


def start(): 
    server.listen()
    print(f"[LISTENING] on server address {SERVER_ADDRESS} and PORT {N_PORT}")
    while True:
        # Waiting for a connection request on n_port
        conn, addr = server.accept() # accept a new connection to this address
        handle_client(conn) # new connection is handled by handle_client
        conn.close() # closes the connection, once purpose has been established 


start()