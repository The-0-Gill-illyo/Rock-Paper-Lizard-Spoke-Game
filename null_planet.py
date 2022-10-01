from ai import Ai
from human import Human
from player import Player

class NullPlanet:

    def __init__(self):
        self.name = ""
        self.player_one = Human()
        self.player_two = None

        ## rules of the game ##

    def welcome_message(self):

        input("Welcome, where the ultimate battle of Rock, Paper, Scissor, Lizard, Spock begins!")

        input("Here are the rules, you are not affriad of Spock's viporizing you!")

        input("Rock crushes Scissors, Scissors cut paper, Paper covers Rock, Rock crushes")

        input("Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,")

        input("Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")

        ## Human vs Human, Human vs Ai ##

    def select_player(self):
        user_input = input("Please choose your oponent: Press 1 for Single Player or 2 for Multiplayer!  ")
        if user_input == "1":
            self.player_two = Ai()
        elif user_input == "2":
            self.player_two = Human()
        else:
            print("Input invalid: Please Choose 1 or 2:  ")
            self.select_player()

    def player_name(self):
        user_input = input("Please enter your Warrior name:  ")
        if user_input == user_input:
            print(f'Great! {user_input} Lets get Rick-rollin!')
        elif self.player_two == Human() and user_input == user_input:
            self.player_name = Human()
            print(f'Great! {user_input} What is is the 2nd Player name?')
        else:
            print("Invalid entry, stop mashing the keys! :P")
            self.player_name()

        ## Game being played znd Round Winner ###

    def play_game(self, round_winner):
        self.wins = 0
        self.looses = 0
        while self.player_one.wins < 2 and self.player_two.wins < 2 and self.player_one.looses > 1 and self.player_two.looses > 1 :
            player_one_choice = self.player_one.throw_gesture()
            player_two_choice = self.player_two.throw_gesture()
            print(f'Player One Gesture: {player_one_choice}')
            print(f'Player Two Gesture: {player_two_choice}')
            return self.play_game()
        if self.player_one.wins == 1:
            print("You won that round")
            self.wins += 1
            return round_winner
        elif self.player_two.looses == 1:
            print("Oh no, you lost that round")
            self.looses += 1
            return round_winner
        elif self.player_two.wins == 1:
            print("Good Job, you won this round!")
            self.wins += 1
            return round_winner
        elif self.player_two.looses == 1:
            print("Ouch, I hate when that happens")
            self.looses += 1
            return round_winner(self.wins and self.looses)
        print(round_winner)
        

            ## Round winner ##
    def round_winner(self):
        self.wins = 0
        self.looses = 0

    def game_winner(self):
        pass

    def wins(self):
        self.wins += 1

    def looses(self):
        self.looses += 1

    def start_game(self):
        self.welcome_message()
        self.select_player()
        self.player_name()
        self.play_game(round_winner=self.select_player)
        self.round_winner()
        self.game_winner()