import sys


def min_value(state, alpha, beta, visited):
    visited.append(state)
    if state.is_terminal():
        return 1
    else:
        value = sys.maxsize
        for a in state.possible_actions():
            value = min(value, max_value(state.action_result(a), alpha, beta, visited))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value


def max_value(state, alpha, beta, visited):
    visited.append(state)
    if state.is_terminal():
        return -1
    else:
        value = -1 * sys.maxsize - 1
        for a in state.possible_actions():
            value = max(value, min_value(state.action_result(a), alpha, beta, visited))
            if beta >= alpha:
                return value
            alpha = max(alpha, value)
        return value


def alpha_beta(state):
    visited = [state]
    if state.is_terminal():
        return None, visited
    else:
        # Alpha initially takes the minimal possible integer value (equivalent to -infinity)
        alpha = -1 * sys.maxsize - 1
        # Beta initially takes the maximal possible integer value (equivalent to +infinity)
        beta = sys.maxsize

        value = -1 * sys.maxsize - 1
        actions = state.possible_actions()
        action = actions[0]
        for a in actions:
            next_value = min_value(state.action_result(a), alpha, beta, visited)
            if next_value > value:
                value = next_value
                action = a
        return action, visited
