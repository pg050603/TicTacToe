import numpy as np

board = np.array(['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X']).reshape(3, 3)

# X or O wins if 3 of their tiles are in consecutive sequence of 3
x_win = np.array(3 * ['X'])
o_win = np.array(3 * ['O'])

# Store winning positions (diagonals, rows, and columns) from the board in the list winning positions
win_positions = [board[0], board[1], board[2], board[:, 0], board[:, 1], board[:, 2],
                 [board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]]]

for win in win_positions:
    # Compare current elements in winning position to winning sequences
    print(win)

    comparison_x = win == x_win

    print(comparison_x.all())
    # If all elements match X-winning sequence, player X wins
    if comparison_x.all() == True:
        winner = str('X')
        game_won = True
        print('X Won')

    comparison_o = win == o_win
    # If all elements match O-winning sequence, player O wins
    if comparison_o.all() == True:
        winner = str('O')
        game_won = True
        print('O won')


winner = None
game_won = False
print('No Winner')

