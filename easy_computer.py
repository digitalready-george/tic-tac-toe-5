import random

class Computer():

    # Constructor
    def __init__(self):
        self.score = 0

    # Calculate a smart random move for the computer
    def valid_move(self, grid):
        available = []
        for cell in grid:
            if type(cell) == int:
                available.append(cell - 1)

        comp = random.choice(available)
        return comp