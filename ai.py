import random
from player import Player



class Ai(Player):

    def __init__(self):
        super().__init__()
        self.gesture_list

    def chosen_gesture(self):
        self.ai_gesture = random.choice(self.gesture_list)
        return self.ai_gesture