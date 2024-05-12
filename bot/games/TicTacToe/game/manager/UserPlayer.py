from telegram import User

from bot.games.TicTacToe.game.core import Player


class UserPlayer:
    def __init__(self, player: Player, user: User):
        self.player = player
        self.user = user

