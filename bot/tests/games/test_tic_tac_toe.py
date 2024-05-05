import pytest
from typing import Tuple, List

from bot.games.TicTacToe.game.core import TicTacToeGame, Player, WinResult, Move, Direction, DrawResult, GAME_RESULT


def get_moves(move_coordinates: Tuple[Tuple[int, int], ...], player: Player) -> List[Move]:
    return [Move(x=x, y=y, player=player) for x, y in move_coordinates]


WIN_MOVES = (
    get_moves(move_coordinates=((0, 0), (1, 0), (2, 0)), player=Player.PLAYER_1),
    get_moves(move_coordinates=((2, 0), (2, 1), (2, 2)), player=Player.PLAYER_2),
    get_moves(move_coordinates=((0, 0), (1, 1), (2, 2)), player=Player.PLAYER_2),
    get_moves(move_coordinates=((0, 2), (1, 1), (2, 0)), player=Player.PLAYER_1),
)

DRAW_MOVES = (
    get_moves(move_coordinates=((0, 0), (0, 2), (1, 1), (2, 1), (1, 2)), player=Player.PLAYER_1) +
    get_moves(move_coordinates=((2, 0), (0, 1), (2, 2), (1, 0)), player=Player.PLAYER_2),
)


@pytest.fixture(scope="function")
def game() -> TicTacToeGame:
    return TicTacToeGame()


@pytest.fixture(autouse=True)
def show_field(game):
    yield
    print()
    print(*game.field, sep='\n')


def test_empty_game(game):
    assert not game.get_result(), "Empty game can't have results!"


@pytest.mark.parametrize(
    'all_moves,expected_result',
    [
        (WIN_MOVES[0], WinResult(winner=Player.PLAYER_1, direction=Direction.column, cells=WIN_MOVES[0])),
        (WIN_MOVES[1], WinResult(winner=Player.PLAYER_2, direction=Direction.row, cells=WIN_MOVES[1])),
        (WIN_MOVES[2], WinResult(winner=Player.PLAYER_2, direction=Direction.diagonal_left_right, cells=WIN_MOVES[2])),
        (WIN_MOVES[3], WinResult(winner=Player.PLAYER_1, direction=Direction.diagonal_right_left, cells=WIN_MOVES[3])),
    ]
)
def test_win_condition(game, all_moves: List[Move], expected_result: GAME_RESULT):
    for move in all_moves:
        game.make_move(move)
    assert game.get_result() == expected_result, "Wrong expected result!"


@pytest.mark.parametrize(
    'all_moves,expected_result',
    [
        (DRAW_MOVES[0], DrawResult()),
    ]
)
def test_draw_condition(game, all_moves: List[Move], expected_result: GAME_RESULT):
    for move in all_moves:
        game.make_move(move)
    assert game.get_result() == expected_result, "Wrong expected result!"
