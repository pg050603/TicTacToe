# Function 1:
"""
Creates a 9 element board of blank tiles (represented by .)

Returns
_________
board : list
1D list for empty board
"""


def initialise_board():
    # Initialise board as list of 9 empty tiles
    board = 9 * ['.']
    return board


# Function 2:
"""
Prints the current board to screen in 3 x 3 pattern

Arguments
__________
board : List
The current board in playing state

Notes
_____
(precondition) Only prints 9 elements, larger board cannot be accurately displayed
"""


def display_board(board):
    # Prints 3 element row in 3 columns (3 x 3) from corresponding element in board
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    return


# Function 3:
"""
Calculates the current turn

Arguments
__________
board : List
The board in current state of play

Returns
_____
turn : integer
The current turn number

Notes
_____
(precondition 1) Number of turns starts from 1
"""


def get_current_turn_number(board):
    # Calculates the number of tiles filled to record the number of previous turns
    played = board.count('X') + board.count('O')

    # 1 + previous turns = current turn number
    turn = 1 + played
    return turn


# Function 4:
"""
Prints the current board to screen in 3 x 3 pattern

Arguments
__________
board : List
The current board in playing state

Returns
_______
player: string
What the name of the current player is (X or O)

Notes
_____
(precondition) Player 1 = X and board tile = X and Player 2 = O and board tile = O
"""


def get_current_player(board):
    # Counts the number of tiles placed by each X and O
    number_x = board.count('X')
    number_o = board.count('O')

    # If the number of tiles placed by X is less than O, the current player will be X. Vica-versa
    if number_x <= number_o:
        player = str('X')
    else:
        player = str('O')
    return player


# Function 5:
"""
Plays a turn of TicTacToe, placing the players tile in specified position and returning the board

Arguments
__________
board : List
The current board in playing state

row_num : Integer
The row position to place the tile

column_num : Integer
The column position to place the tile

Returns
_______
board : List
The board after player tile is placed

Notes
_____
(precondition 1) 1 <= Row position <= 3 Row position must be in the array 'board' defined
(precondition 2) 1 <= Column position <= 3 Column position must be in the array 'board' defined
"""


def play_turn(board, row_num, column_num):
    # Converts row_num & column_num into equivalent board position
    position = 3 * (row_num - 1) + (column_num - 1)

    # If the position is empty, it is available
    # Determine the current player is and place their tile in the position
    if board[position] == '.':
        current_player = get_current_player(board)
        board[position] = current_player

    # If the tile is unavailable, return the board with no placement and inform player
    else:
        board = board
        print("Position already taken")

    return board


# Function 7:
"""
Checks the board to see if a player has won

Arguments
__________
board : List
The current board in playing state

Returns
_______
game_won : boolean
True or False if game has been won or not

winner : String
Name of winning player (X or O)
"""


def check_win(board):
    # X or O wins if 3 of their tiles are in consecutive sequence of 3
    x_win = 3 * ['X']
    o_win = 3 * ['O']

    # Store winning positions (diagonals, rows, and columns) from the board in the list winning positions
    winning_positions = [board[0:3], board[3:6], board[6:9],
                         [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]],
                         [board[0], board[4], board[8]], [board[2], board[4], board[6]]]

    # Loop the list winning positions, if an element matches X_win, player X won the game. Stop looping
    for i in winning_positions:
        if i == x_win:
            winner = str('X')
            game_won = True
            break

        # If an element matches o_win, player O won the game. Stop looping through list
        elif i == o_win:
            winner = str('O')
            game_won = True
            break

        # If there is no match, the game has not been/ yet won and there is no winner
        else:
            game_won = False
            winner = None

    return game_won, winner


# Function 6:
"""
Checks the board to see if the game resulted in a draw

Arguments
__________
board : List
The current board in playing state

Returns
_______
draw : boolean
True or False if game has was drawn or not  
"""


def check_draw(board):
    # Runs check_win & get_current_turn to get turn number and check for game_won
    winner, game_won = check_win(board)
    turn = get_current_turn_number(board)

    # If the game ends (all positions filled), but no one has won, the game results in a draw
    if turn == 10 and not game_won:
        draw = True
    else:
        draw = False

    return draw


# Function 8:
"""
Calls functions 1 to 7 and loops to play a game until the end or a player wins 
"""


def play_game():
    # Initialises and displays empty starting board and loop counter i
    board = initialise_board()
    display_board(board)
    i = int(0)

    # run the loop 10 times
    while i <= 10:
        draw = check_draw(board)

        # If the game is not drawn
        if not draw:
            # Get and print the current turn
            turn = get_current_turn_number(board)
            print('\nCurrent turn: ' + str(turn))

            # Get and print the current player
            current_player = get_current_player(board)
            print('\nCurrent Player: ' + current_player + '\n')

            # Ask the player what row position they want to play and store as row_num
            print('Enter desired row: ')
            row_num = int(input())
            # Ask the player what column position they want to play and store as column_num
            print('\nEnter desired column:')
            column_num = int(input())

            # Call play_turn function, using the user inputted row_num and column_num
            board = play_turn(board, row_num, column_num)
            display_board(board)

            # Check if the game has been won and which player
            winner, game_won = check_win(board)

            # If the game has been won, print winning message to the winning player and end the loop
            if game_won:
                print('\nPlayer ' + winner + ' won the game!')
                break
        # If the game has been drawn, end the loop and ask the player to play again
        else:
            print('\nThe game was drawn. Play again?')
            break
        i += 1
    return

# Comment that was added after git bash, for Task 2.1. The code for functions_ttt is completed :)
