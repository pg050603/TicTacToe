import pytest
from functions_ttt import *


def test_check_game_win_tricky_board():
    board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']
    is_win, player = check_win(board)
    assert (player == 'X')


def test_current_turn():
    board = ['O', '.', 'X', '.', 'X', '.', 'O', 'O', 'X']
    turn = get_current_turn_number(board)
    assert (turn == 7)


def test_current_player():
    board = ['O', 'O', 'X', 'O', 'X', 'O', 'X', '.', '.']
    player = get_current_player(board)
    assert (player == 'X')


def test_play_turn():
    board = ['X', 'O', 'X', '.', '.', '.', '.', '.', '.']
    board = play_turn(board, 1, 1)
    assert (board == ['X', 'O', 'X', '.', '.', '.', '.', '.', '.'])


def test_draw():
    board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    draw = check_draw(board)
    assert (draw == True)


def test_win():
    board = ['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X']
    is_win, player = check_win(board)
    assert (player == 'X')
