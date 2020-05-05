from domain.model.player import Player
from persitence.player.dbo.player_dbo import PlayerDBO


class PlayerRepository:
    def save(self, player: Player) -> Player:
        player_dbo: PlayerDBO = self.__save_sql_alchemy(player.to_dbo())
        return player_dbo.to_model()

    def __save_sql_alchemy(self, player_dbo: PlayerDBO) -> PlayerDBO:
        return player_dbo
