from socket import *
from config import HOST, PORT

clientSocket = socket()

# Host and port info
ip_addr = HOST
port = PORT

# Connect to socket
clientSocket.connect((ip_addr, port))
print("Connected on: ", ip_addr, " port ", str(port))

print("----------------Welcome to the Marble Game!----------------")
print("Please see instructions pdf for rules of the game.\n")

# Send and receive names
name = input(str("What is your name? "))
clientSocket.send(name.encode())
serv_name = clientSocket.recv(port)
serv_name = serv_name.decode()
print(serv_name, "has joined the game. Yayyyyy!")
print("Enter /q to quit the game.")

while True:
    message = clientSocket.recv(port)
    message = message.decode()
    if message == "\winner": # Winner has been declared
        message = clientSocket.recv(port)
        message = message.decode()
        print(message)
        break
    if message == "\q": # Other player quit
        print(serv_name, "has quit the game.")
        break
    client_response = input(message)
    clientSocket.send(client_response.encode())
    if client_response == "\q": # This player has quit
        print("You have quit the game.")
        break

clientSocket.close()
