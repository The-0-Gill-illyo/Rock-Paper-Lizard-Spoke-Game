from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()

    def throw_gesture(self):
        user_choice = input('Choose one geture: Rock, Paper, Scissors, Lizard, Spock.  ')
        if user_choice in self.gesture_list:
            return user_choice
        elif user_choice != self.gesture_list:
            print("Invaid choice: Please Choose again!")
            user_choice = input('Choose one geture: Rock, Paper, Scissors, Lizard, Spock.  ')
            return user_choice
        else:
            self.throw_gesture()