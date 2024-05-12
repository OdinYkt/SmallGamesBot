from abc import ABC

from telegram import User

from bot.games.TicTacToe.game.manager import GameManager


class ManagerState(ABC):
    def __init__(self, manager: GameManager):
        self.manager: GameManager = manager

    async def manage_player(self, user: User, action: str) -> None:
        raise NotImplementedError

    def get_user_state(self, player: User) -> str:
        raise NotImplementedError

