#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by
# reproduction.

from pprint import pprint
import time

def new_game_board(size_of_board):
    return [['.']*size_of_board for i in range(size_of_board)]

def state_of_adjacent_cells(coord, current_board):
    size_of_board = len(current_board)
    row, column = coord
    live_neighbours = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if current_board[(row+i)%size_of_board][(column+j)%size_of_board] == '*':
                live_neighbours += 1
    return live_neighbours


def future_state(coord, current_board):
    row, column = coord
    current_state = current_board[row][column]
    live_neighbours = state_of_adjacent_cells(coord, current_board)
    if current_state == '*':
        if 2 <= live_neighbours <= 3:
            return '*'
    else:
        if live_neighbours == 3:
            return '*'
    return '.'

def evolve_board(current_board):
    size_of_board = len(current_board)
    next_board = new_game_board(size_of_board)
    for row in range(size_of_board):
        for column in range(size_of_board):
            next_board[row][column] = future_state((row,column), current_board)
    return next_board


board = new_game_board(15)

def add_glider(coord, current_board):
    row, column = coord
    current_board[row][column:column+3] = ['.', '*', '.']
    current_board[row+1][column:column+3] = ['.', '.', '*']
    current_board[row+2][column:column+3] = ['*', '*', '*']

add_glider((0,0), board)
add_glider((0,7), board)

while True:
    for row in board:
        print(' '.join([c for c in row]))
    print()
    board = evolve_board(board)
    time.sleep(0.5)