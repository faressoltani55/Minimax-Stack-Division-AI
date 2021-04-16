class State:
    """ A state describes the current configuration of the game aka all the currently developed stacks"""

    def __init__(self, values):
        self._values_ = values

    def indices_of_values_to_split(self):
        indices = []
        for i in range(0, len(self._values_)):
            value = self._values_[i]
            if value > 2:
                indices.append(i)
        return indices

    def is_terminal(self):
        if self.indices_of_values_to_split():
            return False
        else:
            return True

    def possible_actions(self):
        actions = []

        indices = self.indices_of_values_to_split()
        for index in indices:
            value = self._values_[index]
            if value % 2 == 0:
                limit = int(value / 2)
            else:
                limit = int(value / 2) + 1
            for x in range(1, limit):
                actions.append({'index': index, 'values': [x, value - x]})

        return actions

    def action_result(self, action):

        next_values = self._values_[:]
        next_values.pop(action['index'])
        next_values.extend(action['values'])
        return State(next_values)

    def show_stacks(self):
        for value in self._values_:
            print('\33[97m' + '\33[40m' + "    " + str(value) + "    " + '\33[0m')
            print("")