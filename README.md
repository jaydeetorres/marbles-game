# marbles-game
Text-based client/server networked version of marbles game from Netflix's Squid Games

Running the Program
The best way to run this is through the command prompt. These instructions assume that you have Python 3.10 or higher.

The host and port information is in the config.py file. The default is set to run locally but you can adjust this as you see fit. 
 

Open up a Command Prompt through Windows and type in the following: 
	py server.py

You will then be prompted for your name. Type this out and hit ‘enter’
 

Open up another Command Prompt and type in the following:
	py client.py

A similar response will appear.
 

Once the connection is established, the game will start. The command prompt running the server file will have the first turn. Rules of the game are outlined below.

 

Once the game is over (or someone quits) then one last message will be displayed and the connection will be closed.

 
How to Play Marbles
I took inspiration for this from one of the marbles games played in the Netflix TV show Squid Games.

The rules are simple. Each player starts with 10 marbles. One player then chooses to hold any number of their marbles that they have. 
 

The other player must then guess whether the number of marbles held is an odd or even amount. 
 

If the guess is correct, then the marble holding player loses those marbles and they are put in the guessing player’s pile. If the guess is wrong, then the guessing players gives up that number of marbles to the marble holding player.
 

Play continues with players alternating holding and guessing. The game ends when one player has all 20 marbles and thus wins the game.

 
Some notes on the game programming
There are some guardrails for incorrect inputs. For example, a player must choose to hold at least marble and cannot declare they are holding more marbles than they currently own.
 

Also, in the odd/even guess, only “o”, “e”, and “\q” are valid inputs. Otherwise, the program will ask for another entry.

References
I used these two articles for reference. Mostly used this to understand the flow between server message and client response. 
https://www.geeksforgeeks.org/simple-chat-room-using-python/
https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
