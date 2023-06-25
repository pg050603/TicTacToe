import numpy as np


# Function 1:
def initialise_board():
    """
    Creates a 9 element board of blank tiles (represented by .)

    Returns
    _________
    board : list
    1D list for empty board
    """
    # Initialise board as list of 9 empty tiles
    board = np.array(9 * ['.']).reshape(3, 3)
    return board


# Function 2:
def display_board(board):
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
    print(board)
    return


# Function 3:
def get_current_turn_number(board):
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
    # Calculates the number of tiles filled to record the number of previous turns
    turn = np.count_nonzero(board == 'X') + np.count_nonzero(board == 'O') + 1

    return turn


# Function 4:
def get_current_player(board):
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

    # Get the turn number
    turn = get_current_turn_number(board)

    # If the turn number is even, current player is O, else it is X, turns start at 1, X always plays first
    if turn % 2 == 0:
        player = str('O')
    else:
        player = str('X')

    return player


# Function 5:
def play_turn(board, row_num, column_num):
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

    # Conditions to Play Turn: Tile is available, row, column is not out of bounds (i,e. index < 3)
    available = board[row_num][column_num] == '.'

    # If tile is available and in range, play turn
    if available:
        current_player = get_current_player(board)
        board[row_num][column_num] = current_player

    # Tell player if tile is already occupied
    else:
        board = board
        print("Position already taken")

    return board


# Function 7:
def check_win(board):
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
    # X or O wins if 3 of their tiles are in consecutive sequence of 3
    x_win = np.array(3 * ['X'])
    o_win = np.array(3 * ['O'])

    # Store winning positions (diagonals, rows, and columns) from the board in the list winning positions
    win_positions = [board[0], board[1], board[2], board[:, 0], board[:, 1], board[:, 2],
                     [board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]]]

    for win in win_positions:
        # Compare current elements in winning position to X win sequence
        comparison_x = win == x_win

        # If all elements match X-winning sequence, player X wins
        if comparison_x.all():
            winner = str('X')
            game_won = True
            return game_won, winner

        # Compare current elements in winning position to O win sequence
        comparison_o = win == o_win

        # If all elements match O-winning sequence, player O wins
        if comparison_o.all():
            winner = str('O')
            game_won = True
            return game_won, winner

    # If there are no current sequences that win, there is no winner and match is yet to be resolved
    winner = None
    game_won = False
    return game_won, winner


# Function 6:
def check_draw(board):
    """
    Checks the board to see if the game resulted in a draw

    Arguments
    __________
    board : List
    The current board in playing state

    Returns
    _______
    draw : boolean
    True or False if game has been drawn or not
    """
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
def play_game():
    """
    Calls functions 1 to 7 and loops to play a game until the end or a player wins
    """
    # Initialises and displays empty starting board and loop counter i
    board = initialise_board()
    display_board(board)
    draw = check_draw(board)

    # While the game is not drawn
    while not draw:
        # Print the current turn
        turn = get_current_turn_number(board)
        print('\nCurrent turn: ' + str(turn))

        # Print the current player
        current_player = get_current_player(board)
        print('\nCurrent Player: ' + current_player + '\n')

        # Ask the player what row position they want to play and store as row_num
        print('Enter desired row: ')
        row_num = int(input())
        # Ask the player what column position they want to play and store as column_num
        print('\nEnter desired column:')
        column_num = int(input())

        # Check if the position is valid
        position_valid = row_num < 3 and column_num < 3

        # If turn is invalid, recycle turn
        if not position_valid:
            print("Selected tile is outside range")

        # Otherwise, play the turn to board, using play_turn with inputted row and column
        else:
            board = play_turn(board, row_num, column_num)
            display_board(board)

            # Check if the game has been won and which player
            game_won, winner = check_win(board)

            # If the game has been won, print winning message to the winning player and end the loop
            if game_won is True:
                print('\nPlayer ' + winner + ' won the game!')
                return

            # Otherwise, check for a draw
            else:
                draw = check_draw(board)

            # If the game has been drawn, inform player
    print('\nThe game was drawn')

    return

# Comment that was added after git bash, for Task 2.1. The code for functions_ttt is completed :)
