# marbles-game
Text-based client/server networked version of marbles game from Netflix's Squid Games

<h1>Running the Program</h1>
The best way to run this is through the command prompt. These instructions assume that you have Python 3.10 or higher.

The host and port information is in the config.py file. The default is set to run locally but you can adjust this as you see fit. 
 ![host-port](screenshots/screenshot1.png?raw=true)

Open up a Command Prompt through Windows and type in the following: 
	py server.py

You will then be prompted for your name. Type this out and hit ‘enter’
  ![name-prompt](screenshots/screenshot2.png?raw=true)

Open up another Command Prompt and type in the following:
	py client.py

A similar response will appear.

 ![client-start](screenshots/screenshot3.png?raw=true)

Once the connection is established, the game will start. The command prompt running the server file will have the first turn. Rules of the game are outlined below.

![turn](screenshots/screenshot4.png?raw=true)

Once the game is over (or someone quits) then one last message will be displayed and the connection will be closed.
 ![game-over](screenshots/screenshot5.png?raw=true)
 
<h1>Game Rules: How to Play Marbles</h1>
I took inspiration for this from one of the marbles games played in the Netflix TV show Squid Games.

The rules are simple. Each player starts with 10 marbles. One player then chooses to hold any number of their marbles that they have. 
![hold](screenshots/screenshot6.png?raw=true)

The other player must then guess whether the number of marbles held is an odd or even amount. 
![guess](screenshots/screenshot7.png?raw=true)

If the guess is correct, then the marble holding player loses those marbles and they are put in the guessing player’s pile. If the guess is wrong, then the guessing players gives up that number of marbles to the marble holding player.
![correct-incorrect](screenshots/screenshot8.png?raw=true)

Play continues with players alternating holding and guessing. The game ends when one player has all 20 marbles and thus wins the game.
![winner](screenshots/screenshot9.png?raw=true)
 
<h1>Additional notes on the game programming</h1>
There are some guardrails for incorrect inputs. For example, a player must choose to hold at least marble and cannot declare they are holding more marbles than they currently own.
![incorrect-inputs](screenshots/screenshot10.png?raw=true)

Also, in the odd/even guess, only “o”, “e”, and “\q” are valid inputs. Otherwise, the program will ask for another entry.
![valid-inputs](screenshots/screenshot11.png?raw=true)

<h1>References</h1>
I used these two articles for reference. Mostly used this to understand the flow between server message and client response. 
https://www.geeksforgeeks.org/simple-chat-room-using-python/

https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
