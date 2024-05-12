from telegram import User

from bot.games.TicTacToe.game.manager.GameManager import GameManager


# часть GameManager ?
def get_manager_single(player: User) -> GameManager:
    return GameManager(
        player_1=player
    )