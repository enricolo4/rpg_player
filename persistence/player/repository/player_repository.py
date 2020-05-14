from domain.model.player import Player
from persistence import session
from persistence.player.dbo.player_dbo import PlayerDBO, player_to_dbo


class PlayerRepository:
    def save(self, player: Player) -> Player:
        player_converted_to_dbo: PlayerDBO = player_to_dbo(player)
        session.add(player_converted_to_dbo)

        return session.query().filter(PlayerDBO.id == player_converted_to_dbo.id).to_model()




