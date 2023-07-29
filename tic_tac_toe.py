# George ElMassih (also bennett gillig)
# July 19, 2023

import user
import hard_computer
import view

import tkinter as tk

# Make a new empty grid
def init_grid():
    return list(range(1,10))

# Place markers on the grid
def place_marker(buttons, grid, index, symbol):
    buttons[index].config(text=symbol)
    grid[index] = symbol
    
def user_move(buttons, status, computer, grid, index):
    print(index)
    
    # check if I can place
    if not ("X" != grid[index] != "O"):
        status.config(text=f"Cannot click thingy {index+1}")
        return
        
    # place
    place_marker(buttons, grid, index, "O")

    # check win and draw
    if check_win(grid, status): return
    
    # do computer
    move = computer.valid_move(grid)
    print(move)
    place_marker(buttons, grid, move, "X")
    
    # check win and draw
    if check_win(grid, status): return
    
    status.config(text=f"Clicked thingy {index+1}")
    
# Check if somebody won
def check_win(grid, status):
    win = winning_row(grid[0:3]) or \
    winning_row(grid[3:6]) or \
    winning_row(grid[6:9]) or \
    winning_row(grid[0:9:3]) or \
    winning_row(grid[1:9:3]) or \
    winning_row(grid[2:9:3]) or \
    winning_row(grid[0:9:4]) or \
    winning_row(grid[2:7:2])
    if win:
        status.config(text=f"{win}s win!")
        return True
        
    if stalemate(grid):
        status.config(text="It's a draw!")
        return True
        
    return False
    

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
    root = tk.Tk()
    root.geometry("150x150")
    root.title("tic-tac-toe")
    
    status = tk.Label(root, text="Pick a square")
    status.pack()
    
    frame = tk.Frame(root)
    frame.pack()
    
    computer = hard_computer.Smart_Computer()
    grid = [*range(1,10)]

    buttons = []
    for i in range(9):
        command = lambda i=i: user_move(buttons, status, computer, grid, i)
        buttons.append(tk.Button(frame, text=i, command=command))
        buttons[i].grid(row=i//3, column=i%3, padx=5, pady=5)
        
    
    root.mainloop()
