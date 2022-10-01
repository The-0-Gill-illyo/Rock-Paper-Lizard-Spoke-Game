from random import random
from player import Player
import random



class Ai(Player):

    def __init__(self):
        super().__init__()
        self.gesture_list

    def throw_gesture(self):
        ai_gesture = random.choice(self.gesture_list)
        return ai_gesture