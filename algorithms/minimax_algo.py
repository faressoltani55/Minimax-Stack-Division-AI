import sys


def min_value(state, visited):
    visited.append(state)
    if state.is_terminal():
        return 1
    else:
        # Initialized with maximal possible integer value
        value = sys.maxsize
        for a in state.possible_actions():
            value = min(value, max_value(state.action_result(a), visited))
        return value

def max_value(state, visited):
    visited.append(state)
    if state.is_terminal():
        return -1
    else:
        # Initialized with minimal possible integer value
        value = -1 * sys.maxsize - 1
        for a in state.possible_actions():
            value = max(value, min_value(state.action_result(a), visited))
        return value

def minimax_decision(state):
    visited = [state]
    if state.is_terminal():
        return None, visited
    else:
        value = -1 * sys.maxsize - 1
        actions = state.possible_actions()
        action = actions[0]
        for a in actions:
            next_value = min_value(state.action_result(a), visited)
            if next_value > value:
                value = next_value
                action = a
        return action, visited
