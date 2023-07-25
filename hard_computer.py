from computer import Computer
import random
class Smart_Computer(Computer):

    # Calculate a smart move for the computer
    def valid_move(self, grid):
        winning_rows = [grid[0:3],
        grid[3:6],
        grid[6:9],
        grid[0:9:3],
        grid[1:9:3],
        grid[2:9:3],
        grid[0:9:4],
        grid[2:7:2]]

        for row in winning_rows:
            if self.smart_helper(row):
                for cell in row:
                    if type(cell) == int:
                        return cell
    
        return Computer.valid_move(self, grid)


    def smart_helper(self, row):
        return row[0] == row[1] or row[1] == row[2] or row[0] == row[2]
        