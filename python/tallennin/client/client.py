import socket
import sys

def client():

    prompt_msg = "Anna tallennettava viesti, lataa viestit (V) tai lopeta (L)\n"
    host = "localhost"
    port = 15000

    client_socket = socket.socket()
    client_socket.connect((host,port))
   
    message = input(prompt_msg)
    if message.lower().strip() == "l":
        client_socket.close()
        sys.exit()
    else:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()

if __name__=="__main__":
    client()