class User():

    # Constructor
    def __init__(self):
        self.score = 0

    # Processes user inputs
    def valid_input(self, grid):
        while True:
            user_input = input("Select a position from 1 to 9: ")
            if user_input.isnumeric() and isinstance(grid[int(user_input) - 1], int) and int(user_input) >= 1 and int(user_input) <= 9:
                return int(user_input)
            else:
                print("Invalid Choice")
    