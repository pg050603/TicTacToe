import pytest
from functions_ttt import *


def test_check_game_win_tricky_board():
    board = np.array(['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']).reshape(3,3)
    is_win, player = check_win(board)
    assert (player == 'X')


def test_current_turn():
    board = np.array(['O', '.', 'X', '.', 'X', '.', 'O', 'O', 'X']).reshape(3,3)
    turn = get_current_turn_number(board)
    assert (turn == 7)


def test_current_player():
    board = np.array(['.', '.', 'X', 'O', 'X', 'O', 'X', '.', '.']).reshape(3,3)
    player = get_current_player(board)
    assert (player == 'O')


def test_play_turn():
    board = np.array(['X', 'O', 'X', '.', '.', '.', '.', '.', '.']).reshape(3,3)
    board_played = play_turn(board, 1, 1)
    comparison = board_played == np.array(['X', 'O', 'X', '.', 'O', '.', '.', '.', '.']).reshape(3,3)
    assert comparison.all() == True


def test_draw():
    board = np.array(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']).reshape(3,3)
    draw = check_draw(board)
    assert (draw == True)


def test_win():
    board = np.array(['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X']).reshape(3,3)
    is_win, player = check_win(board)
    assert (player == 'X')
