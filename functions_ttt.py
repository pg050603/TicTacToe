# Function 1:
def initialise_board():
    board = 9 * ['.']
    return board


# Function 2:
def display_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    return


# Function 3:
def get_current_turn_number(board):
    played = board.count('X') + board.count('O')
    turn = 1 + played
    return turn


# Function 4:
def get_current_player(board):
    number_x = board.count('X')
    number_o = board.count('O')

    if number_x <= number_o:
        player = str('X')
    else:
        player = str('O')
    return player


# Function 5:
def play_turn(board, row_num, column_num):
    position = 3 * (row_num - 1) + (column_num - 1)
    if board[position] == '.':
        current_player = get_current_player(board)
        board[position] = current_player
    else:
        board = board
        print("Position already taken")

    return board


# Function 7:
def check_win(board):
    x_win = 3 * ['X']
    o_win = 3 * ['O']
    winning_positions = [board[0:3], board[3:6], board[6:9],
                         [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]],
                         [board[0], board[4], board[8]], [board[2], board[4], board[6]]]

    for i in winning_positions:
        if i == x_win:
            winner = str('X')
            game_won = True
            break
        elif i == o_win:
            winner = str('O')
            game_won = True
            break
        else:
            game_won = False
            winner = None

    return winner, game_won


# Function 6:
def check_draw(board):
    winner, game_won = check_win(board)
    turn = get_current_turn_number(board)
    if turn == 10 and not game_won:
        draw = True
    else:
        draw = False

    return draw


# Function 8:
def play_game():
    board = initialise_board()
    display_board(board)
    i = int(0)

    while i <= 10:
        draw = check_draw(board)

        if not draw:
            turn = get_current_turn_number(board)
            print('\nCurrent turn: ' + str(turn))

            current_player = get_current_player(board)
            print('\nCurrent Player: ' + current_player + '\n')

            print('Enter desired row: ')
            row_num = int(input())

            print('\nEnter desired column:')
            column_num = int(input())

            board = play_turn(board, row_num, column_num)
            display_board(board)

            winner, game_won = check_win(board)

            if game_won:
                print('\nPlayer ' + winner + ' won the game!')
                break
        else:
            print('\nThe game was drawn. Play again?')
            break
        i += 1
    return
