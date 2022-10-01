from ai import Ai
from human import Human
from null_planet import NullPlanet
from player import Player

play = NullPlanet()

play.start_game()

play.play_game(round_winner=play.select_player)

play.round_winner()

play.game_winner()

play.wins()

play.looses()