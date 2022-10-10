from ai import Ai
from human import Human
from player import Player

class NullPlanet:

    def __init__(self):
        self.name = ""
        self.player_one = Human()
        self.player_two = Human()
        self.player_ai = Ai()

        ## rules of the game ##

    def welcome_message(self):

        input("Welcome unlucky victim, this is where the ultimate battle of Rock, Paper, Scissor, Lizard, Spock begins! (PRESS ENTER TO CONTINUE)")

        input("Here are the rules, if you are not affriad of Spock viporizing you! (PRESS ENTER TO CONTINUE)" )

        input("Rock crushes Scissors, Scissors cut paper, Paper covers Rock, Rock crushes Lizard, (PRESS ENTER TO CONTINUE)")

        input("Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, (PRESS ENTER TO CONTINUE)")

        input("Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock (PRESS ENTER TO CONTINUE)")

        ## Human vs Human, Human vs Ai ##

    def select_player(self):
        user_input = input("Would you like to play Single Player mode against an AI? Yes or No?  ")
        if user_input == "Yes":
            self.player_two = Ai()
            self.player_one.enter_name()
            print(f'Great! {user_input} Lets get Rick-rollin!')
            return
        elif user_input == "No":
            input("Please enter your Warrior names: (PRESS ENTER TO CONTINUE) ")
            self.player_one.enter_name()
            self.player_two.enter_name()
            print(f'Great! {self.player_one.name} and {self.player_two.name} Lets get Rick-rollin!')
            return
        else:
            print("You must choose or feel the rath of Spoke!  ")
            self.select_player()


        ## Game being played and Round Winner ###

    def play_game(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            player_one_choice = self.player_one.choose_gesture()
            player_two_choice = self.player_two.choose_gesture()
            self.game_battle()

        self.game_winner()    

    def game_battle(self):
          if self.player_one == self.player_two:
            print("Socking! It's a tie!")
            if self.player_one.chosen_gesture == 'rock':
                if self.player_one.chosen_gesture == 'paper':
                    print("Paper beats rock! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Rock crushes lizard! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Spock vaporizes rock! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'scissors':
                print("Rock smashes scissors! Player 1 wins!")
                self.player_one.wins += 1
            if self.player_one.chosen_gesture == 'scissors':
                if self.player_two.chosen_gesture == 'paper':
                    print("Scissors cut paper! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Scissors decapitates lizard! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Spock SNASH scissors! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Rock SMASH scissors! Player 2 wins!")
                self.player_two.wins += 1
            if self.player_one.chosen_gesture == 'paper':
                if self.player_two.chosen_gesture == 'scissors':
                    print("Scissors cut paper! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Lizard eats paper! MMM Fiber! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Paper disproves Spock! Take that nerd! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Paper covers Rock! Player 1 wins!")
                self.player_one.wins += 1
            if self.player_one.chosen_gesture == 'lizard':
                if self.player_two.chosen_gesture == 'scissors':
                    print("Scissors decapitate lizard! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'paper':
                print("Lizard eats paper! MMM Fiber! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Lizard poisons Spock! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Rock crushes lizard! Player 2 wins!")
                self.player_two.wins += 1
            if self.player_one.chosen_gesture == 'spock':
                if self.player_two.chosen_gesture == 'scissors':
                    print("Spock SNASH scissors! Player 1 wins!")
                self.player_one.wins += 1
            elif self.player_two.chosen_gesture == 'paper':
                print("Paper disproves Spock! Take that nerd! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Lizard poisons Spock! Player 2 wins!")
                self.player_two.wins += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Spock vaporizes Rock! Player 1 wins!")
                self.player_one.wins += 1

    def game_winner(self):
        if (self.player_one.wins == 2):
            print(f'{self.player_one.name} wins the game!')
        elif (self.player_two.wins == 2):
            print(f'{self.player_two.name} wins the game!')
        

    def start_game(self):
        self.welcome_message()
        self.select_player()
        self.play_game()
        self.game_winner()
        


    
        

   