from telegram import User

from .GameManager import GameManager
from .states import ManagerState


class ManagerFactory:

    @classmethod
    def get_manager_single_game(cls, user: User):
        return GameManager(
            user_1=user,
            # state= ?
        )
