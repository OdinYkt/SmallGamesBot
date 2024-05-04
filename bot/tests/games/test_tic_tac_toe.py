import pytest
from typing import Dict, Tuple

from bot.games.TicTacToe.core import TicTacToeGame, Player, WinResult, Move, Direction


@pytest.fixture(scope="function")
def game() -> TicTacToeGame:
    return TicTacToeGame()


@pytest.fixture(autouse=True)
def show_field(game):
    yield
    print()
    print(*game.field, sep='\n')


def test_empty_game(game):
    assert not game.winner, "Empty field can't have winner!"
    assert game.have_empty_cells(), "Empty field must have empty cells"


@pytest.mark.parametrize(
    'all_moves,expected_result',
    [
    (
            {
                Player.PLAYER_1: (Move(0, 0), Move(1, 0), Move(2, 0)),
            },
            WinResult(winner=Player.PLAYER_1, direction=Direction.column, index=0)
    ),
    (
            {
                Player.PLAYER_2: (Move(2, 0), Move(2, 1), Move(2, 2))
            },
            WinResult(winner=Player.PLAYER_2, direction=Direction.row, index=2)
    ),
    (
            {
                Player.PLAYER_2: (Move(0, 0), Move(1, 1), Move(2, 2))
            },
            WinResult(winner=Player.PLAYER_2, direction=Direction.diagonal_left_right)
    ),
    (
            {
                Player.PLAYER_1: (Move(2, 0), Move(1, 1), Move(0, 2))
            },
            WinResult(winner=Player.PLAYER_1, direction=Direction.diagonal_right_left)
    )
    ]
)
def test_win_condition(game, all_moves: Dict[Player, Tuple[Move]], expected_result: WinResult):
    for player, moves in all_moves.items():
        for move in moves:
            game.make_move(player, move)
    assert game.winner == expected_result, "Wrong expected result!"
