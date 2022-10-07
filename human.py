from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.choosen_gesture = self.gesture_list

    def enter_name(self):
        self.name = input("Please enter your name!")

    def choose_gesture(self):
        self.choosen_gesture = self.gesture_list[0:4]
        user_choice = input('Choose geture: Rock, Paper, Scissors, Lizard, Spock.  ')
        if user_choice == self.gesture_list[0]:
            print('You picked rock!')
            self.chosen_gesture = self.gesture_list[0]
        elif user_choice == self.gesture_list[1]:
            print('You chose paper!')
            self.chosen_gesture = self.gesture_list[1]
        elif user_choice == self.gesture_list[2]:
            print('You chose scissors!')
            self.chosen_gesture = self.gesture_list[2]
        elif user_choice == self.gesture_list[3]:
            print('You chose lizard!')
            self.chosen_gesture = self.gesture_list[3]
        elif user_choice== self.gesture_list[4]:
            print('You chose spock!')
            self.chosen_gesture = self.gesture_list[4]
        else:
            print('not a valid option')
            self.choose_gesture()