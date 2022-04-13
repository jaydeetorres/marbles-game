class marbles:
    def __init__(self, host_name, client_name) -> None: # Initialize game
        self.host_marbles = 10
        self.client_marbles = 10
        self.marbles_held = 0
        self.player_holding = "host"
        self.even = False
        self.winner = None
        self.host_name = host_name
        self.client_name = client_name
    
    def check_valid_hold(self, num_marbs) -> bool:
        if num_marbs < 1: # Cannot hold 0 marbles
            return False
        
        # Check if marbles held is equal to or less than marbles owned
        if self.player_holding == "host":
            if num_marbs > self.host_marbles:
                return False
            else:
                return True
        else:
            if num_marbs > self.client_marbles:
                return False
            else:
                return True
    
    def get_player_turn(self) -> str:
        return self.player_holding

    def hold_marbles(self, num_marbs) -> bool:
        if not self.check_valid_hold(num_marbs):
            return False

        # Calculate odd or even marbles held
        if num_marbs % 2 == 0:
            self.even = True
        else:
            self.even = False
        
        self.marbles_held = num_marbs
        
        return True

    def check_player_guess(self, guess) -> bool:
        # Check if guess is correct or not
        if guess == "e" and self.even:
            return True
        elif guess == "o" and not self.even:
            return True
        else:
            return False
    
    def check_winner(self) -> bool:
        # Check for a winner
        if self.host_marbles < 1:
            self.winner = self.client_name
            return True

        if self.client_marbles < 1:
            self.winner = self.host_name
            return True

        return False
    
    def get_winner(self) -> str:
        return self.winner

    def marble_swap(self, winner) -> None:
        if winner == "host": # Host won and gets marbles
            self.client_marbles -= self.marbles_held
            self.host_marbles += self.marbles_held
        else: # Client won and gets marbles
            self.client_marbles += self.marbles_held
            self.host_marbles -= self.marbles_held

    def game_turn(self, marbles_held, guess) -> bool:
        if not self.hold_marbles(marbles_held):
            return False
        
        if self.check_player_guess(guess): # Guess is right so holder loses marbles
            if self.player_holding == "host":
                self.marble_swap("client")
            else:
                self.marble_swap("host")
        else: # Guess is wrong so holder gains marbles
            if self.player_holding == "host":
                self.marble_swap("host")
            else:
                self.marble_swap("client")
        
        # Switch sides
        if self.player_holding == "host":
            self.player_holding = "client"
        else:
            self.player_holding = "host"
        
        return True

    def check_game_state(self) -> str:
        return str("\n-----Marbles Remaining-----\n" + self.host_name + " " + str(self.host_marbles) + " / " + self.client_name + " " + str(self.client_marbles))

if __name__ == "__main__": # used this to test workflow for running the game
    winner = False
    game = marbles()

    while not winner:
        print("The", game.get_player_turn(), "is holding the marbles.")
        hold_marbles = input(str("How many marbles to hold? "))

        if not game.check_valid_hold(int(hold_marbles)):
            print("Invalid input.")
        
        else:
            guess = input(str("Is your guess odd or even? (o/e)"))

            game.game_turn(int(hold_marbles), guess)

            print(game.check_game_state())

            if game.check_winner():
                winner = True
                print("The winner is", game.get_winner())
