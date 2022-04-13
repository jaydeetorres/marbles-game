from socket import *
from config import HOST, PORT
from marbles import *

def quit_game(quitter): # Used to end game and close socket
    if quitter == "server":
        print("You have quit the game.")
        message = "\q"
        conn.send(message.encode())
    else:
        print(client_name, "has quit the game.")
    serverSocket.close()

# Host and port info - see config file
ip_addr = HOST
port = PORT

# Establish socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((ip_addr, port))
serverSocket.listen(100)

print("Server listening on: ", ip_addr, " port ", str(port))

print("----------------Welcome to the Marble Game!----------------")
print("Please see instructions pdf for rules of the game.\n")

name = input(str("What is your name? "))
print("Please wait for the other player to join...")

# Accept client joining socket
conn, addr = serverSocket.accept()

# Receive name of other player and send name back
client_name = conn.recv(port)
client_name = client_name.decode()
print(client_name, "has joined the game. Yayyyy!")
print("Enter /q to quit the game.")
conn.send(name.encode())

# Initialize game
winner = False
game = marbles(name, client_name)
message = "\n"

while not winner:
    print(game.check_game_state(), "\n")

    if game.get_player_turn() == "host": # Case if it is hosts turn to hold marbles
        hold_marbles = input(str("It is your turn to hold the marbles. \nHow many would you like to hold? "))
        
        if hold_marbles == "\q": 
            quit_game("server")
            break

        while not game.check_valid_hold(int(hold_marbles)):
            hold_marbles = input(str("Invalid input. How many marbles would you like to hold? "))
        
        message = message + game.check_game_state() + "\n" + name + " is holding marbles. Is your guess odd or even? (o/e) "
        conn.send(message.encode())
        client_response = conn.recv(port)
        client_response = client_response.decode()

        while client_response != "o" and client_response != "e" and client_response != "\q": # Loop if response is not valid - these are placed throughout code
            message = "Invalid input. Is your guess odd or even? (o/e) "
            conn.send(message.encode())
            client_response = conn.recv(port)
            client_response = client_response.decode()
        
        if client_response == "\q":
            quit_game("client")
            break
        
        guess = client_response
    
    else: # Case if it is clients turn to hold marbles
        message = message + game.check_game_state() + "\nIt is your turn to hold the marbles. \nHow many would you like to hold? "
        conn.send(message.encode())
        client_response = conn.recv(port)
        client_response = client_response.decode()

        if client_response == "\q":
            quit_game("client")
            break

        while not game.check_valid_hold(int(client_response)): # Loop if response is not valid
            message = "Invalid input. How many marbles would you like to hold? "
            conn.send(message.encode())
            client_response = conn.recv(port)
            client_response = client_response.decode()
            if client_response == "\q":
                quit_game("client")
                break
        if client_response == "\q":
            break
        
        hold_marbles = client_response
        guess = input(str(name + " is holding marbles. Is your guess odd or even? (o/e) "))
        while guess != "o" and guess != "e" and guess != "\q":
            guess = input(str("Invalid input. Is your guess odd or even? (o/e) "))
        
        if guess == "\q":
            quit_game("server")
            break
            
    game.game_turn(int(hold_marbles), guess)

    # Response for marbles held and odd/even guess
    if guess == "e":
        message = hold_marbles + " marbles were held and the guess was even.\n"
    else:
        message = hold_marbles + " marbles were held and the guess was odd.\n"

    print(message)

    # Check for a winner
    if game.check_winner():
        winner = True
        win_send = str("\winner")
        conn.send(win_send.encode())

        message = str(message + "\n------------------------------------------\nGame over! The winner is " + game.get_winner() + "\n------------------------------------------\n")
        conn.send(message.encode())
        
        print(str("\n------------------------------------------\nGame over! The winner is " + game.get_winner() + "\n------------------------------------------\n"))
        serverSocket.close()
