from domain.model.player import Player
from persistence.player.repository.player_repository import PlayerRepository


class PlayerService:
    def __init__(self):
        self.__player_repository = PlayerRepository()

    def save(self, player: Player) -> Player:
        return self.__player_repository.save(player)

