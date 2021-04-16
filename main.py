# This is a sample Python script.
from game.game_utils import *
from game.state import State
from algorithms.minimax_algo import *
from algorithms.alphabeta_algo import *

import matplotlib.pyplot as plt
import os

os.system('COLOR')


# Controlling the values given by the user (integers in a limited interval)
def input_control(interval=None, description=""):
    value = input(description)
    while not value.isnumeric():
        value = input("Please enter one number!")
    value = int(value)
    if interval is not None:
        while value not in interval:
            print("The value must be in this interval: ")
            print(interval)
            value = input_control(interval)

    return value


# Getting the decision
def get_user_choice(state):
    values = state._values_
    value = input_control(interval=list(filter(lambda value: value >= 3, values)), description="Choose a number to "
                                                                                             "divide: ")
    if value % 2 == 0:
        possible_division_values = list(range(1, int(value / 2)))
    else:
        possible_division_values = list(range(1, int(value / 2) + 1))

    division_value = input_control(interval=possible_division_values, description="Choose how to divide it (Only "
                                                                                      "enter one of the numbers) ")
    action = {'index': state._values_.index(value), 'values': [division_value, value - division_value]}
    return state.action_result(action)


if __name__ == '__main__':

    print("Ready to play Stack Division? ")

    name = input("Please enter your name: ")

    initial_stack_value = input_control(interval=None,
                              description="Please enter the initial stack value : ")

    print("Please choose the playing mode for your opponent (The output score of the game is independent of the "
          "chosen mode) \n")
    print("1 - Slow Mode (Minimax Algorithm)")
    print("2 - Faster Mode (AlphaBeta Algorithm: enhancement so that the computer plays faster, not better)")
    mode = input_control(interval=[1, 2], description="Choose the mode number: ")

    if int(mode) == 1:
        algorithm = minimax_decision
    else:
        algorithm = alpha_beta

    current_state = State([initial_stack_value])

    # Random starting player
    current_player = randomize_player()
    temp_state = State(current_state._values_[:])
    max_rounds = 0
    visited_lengths = []
    while not current_state.is_terminal():
        # Printing the current configuration
        print("Current stacks: ")
        current_state.show_stacks()

        if current_player == Player.Min:

            print('\33[34m'+ "It's currently your turn," + name + " !" + '\33[0m')
            current_state = get_user_choice(current_state)

        else:

            max_rounds = max_rounds + 1
            print('\33[34m' + "It's currently your opponent's turn!" + '\33[0m')
            # Using a temporary state to run the minimax/alphabeta algortihms on
            temp_state._values_ = current_state._values_[:]
            # Running the algorithm
            optimal_action, visited = algorithm(temp_state)
            # Keeping up with the number of visited nodes during the algorithm
            visited_lengths.append(len(visited))
            # Doing the action suggested by the algorithm
            current_state = current_state.action_result(optimal_action)

        current_player = switch_player(current_player)

    if current_state.is_terminal():
        print("Final configuration")
        current_state.show_stacks()
        if current_player == Player.Min:
            print('\33[91m'+"You lost :(")
        else:
            print('\33[92m'+"You WON!!!!")

    print("Visited nodes by max player (the machine) per round using the algorithm: " + algorithm.__name__)
    max_round_names = ["Round "+str(round_number) for round_number in range(1, max_rounds + 1)]
    plt.bar(max_round_names, visited_lengths, width=0.5)
    plt.show()
