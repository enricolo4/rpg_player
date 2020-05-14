from domain.model.player import Player
from persistence.player.dbo.player_dbo import PlayerDBO, player_to_dbo


class PlayerRepository:
    def save(self, player: Player) -> Player:
        player_converted_to_dbo: PlayerDBO = player_to_dbo(player)
        player_dbo = self.__save_sql_alchemy(player_converted_to_dbo)

        return player_dbo.to_model()

    def __save_sql_alchemy(self, player_dbo: PlayerDBO) -> PlayerDBO:
        return player_dbo
