from telegram import User

from bot.common.dataclasses_ import Position

from bot.games.TicTacToe.game.manager.GameManager import GameManager
from bot.games.TicTacToe.game.manager.UserPlayer import UserPlayer
from bot.games.TicTacToe.game.core import Move, Player, CellMarkedException, OutOfFieldException


from .ManagerState import ManagerState


class MainGameState(ManagerState):
    def __init__(self, manager: GameManager):
        super(MainGameState, self).__init__(manager=manager)
        self.turn: Player = Player.PLAYER_1

    def change_turn(self):
        if self.turn == Player.PLAYER_1:
            self.turn = Player.PLAYER_2
        else:
            self.turn = Player.PLAYER_1

    async def manage_player(self, user: User, action: str) -> None:
        user_player = self.manager.get_user_player(user=user)
        if self.turn == user_player.player:
            self.make_move(user_player=user_player, action=action)
            print(f'Игрок {user_player} сделал ход')
            self.change_turn()
            # TODO
            #   Оповещаем второго игрока
            return

        # что если не ход игрока
        ...

    def get_user_state(self, player: User) -> str:
        ...

    def make_move(self, user_player: UserPlayer, action: str):
        move = Move(
            pos=self.get_position(action),
            player=user_player.player,
        )
        try:
            self.manager.game.make_move(move)
        except CellMarkedException:
            ...
        except OutOfFieldException:
            ...


    @staticmethod
    def get_position(action: str) -> Position:
        # get position from data keyboard
        return Position(x=0, y=0)