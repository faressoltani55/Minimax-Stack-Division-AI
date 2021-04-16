from random import randint
import enum


class Player(enum.Enum):
    Max = "Max"
    Min = "Min"


def randomize_player():
    # generate a random number
    if randint(0, 1) == 0:
        return Player.Min
    else:
        return Player.Max


def switch_player(current_player):
    # switch the players
    if current_player == Player.Min:
        return Player.Max
    else:
        return Player.Min


