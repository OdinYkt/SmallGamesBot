from typing import Optional, Type

from telegram import User

from bot.common.utils import Counter, split_to
from bot.common.dataclasses_ import Position

from bot.games.TicTacToe.game.core import TicTacToeGame, Player
from .states import ManagerState
from .UserPlayer import UserPlayer

DATA_TO_FIELD_MAP = {Counter.give_one(): Position(x=x, y=y) for x in range(SIZE) for y in range(SIZE)}


class GameManager:
    # Паттерн наблюдатель
    # Паттерн состояние
    def __init__(self, user_1: User, user_2: Optional[User] = None, start_state: Optional[Type[ManagerState]] = None):
        self.game = TicTacToeGame()

        # TODO
        #   WHAT IF user_2 = None ? (bot)

        self._players = {}

        self.user_1 = user_1
        self.user_2 = user_2

        # TODO WHAT IF NONE?
        self.state = None
        self.set_state(start_state)

    def get_user_player(self, user: Optional[User] = None, player: Optional[Player] = None) -> UserPlayer:
        pass

    def set_state(self, new_state: Type[ManagerState]):
        self.state = new_state(self)

    async def manage_player(self, user: User, action: str) -> None:
        await self.state.manage_player(user=user, action=action)

    def get_user_state(self, player: User) -> str:
        ...

    @staticmethod
    def _get_data_to_field_map():
        return DATA_TO_FIELD_MAP


FIELD_KEYS = FIELD_CELLS.keys()
row1, row2, row3 = split_to([*FIELD_KEYS], chunk_count=3)
rows = (row1, row2, row3)


empty_field = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=EMPTY.EMPTY.value, callback_data=key) for key in row] for row in rows]
)