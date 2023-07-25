# George ElMassih
# July 19, 2023

import user
import easy_computer
import hard_computer
import view

# Main Function
# Plays Tic-Tac-Toe
def tic_tac_toe():
    # Initialize the empty grid
    grid = init_grid()
    game_over = False
    player = user.User()

    difficulty = input("Easy or Hard?")
    if difficulty == "Easy":
        comp = easy_computer.Computer()
    elif difficulty == "Hard":
        comp = hard_computer.Hard_Computer()
    else:
        comp = easy_computer.Computer()
    
    while not game_over:
        view.print_grid(grid)
        # Accept user input
        player_move = player.valid_input(grid)
        # Place user's X on grid
        place_marker(grid, player_move, "X")

        # Generate a random computer move
        computer_move = comp.valid_move(grid)
        # Place computer's O on grid
        grid = place_marker(grid, computer_move, "o")
        
        # Check if someone has won the game
        game_over = check_win(grid)
        
    # Game has ended
    if game_over == "X":
        print("Congrats! You won!")
    elif game_over == "o":
        print("Oh no! You lost!")
    else:
        print("There's been a stalemate!")

# Helper Funcions

# Make a new empty grid
def init_grid():
    return list(range(1,10))

# Place markers on the grid
def place_marker(grid, index, symbol):
    grid[index-1] = symbol
    return grid

# Check if somebody won
def check_win(grid):
    if stalemate(grid):
        return "Draw"
    else:
        win = winning_row(grid[0:3]) or \
        winning_row(grid[3:6]) or \
        winning_row(grid[6:9]) or \
        winning_row(grid[0:9:3]) or \
        winning_row(grid[1:9:3]) or \
        winning_row(grid[2:9:3]) or \
        winning_row(grid[0:9:4]) or \
        winning_row(grid[2:7:2])
        return win

# Check for a stalemate
def stalemate(grid):
    return all(isinstance(cell, str) for cell in grid)

# Check if three symbols in a list match
def winning_row(row):
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    else:
        return False

if __name__ == "__main__":
    tic_tac_toe()