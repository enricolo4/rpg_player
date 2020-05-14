import uuid

from sqlalchemy import Column, String

from domain.model.player import Player
from persistence.base_dbo import BaseDBO


class PlayerDBO(BaseDBO):
    __tablename__ = "player"

    name = Column(String)
    nickname = Column(String)
    birth_date = Column(String)
    email = Column(String)
    password = Column(String)

    def to_model(self) -> Player:
        return Player(
            id=uuid.UUID(self.id),
            name=self.name,
            nickname=self.nickname,
            birth_date=self.birth_date,
            email=self.email,
            password=self.password
        )


def player_to_dbo(player: Player) -> PlayerDBO:
    return PlayerDBO(
        name=player.name,
        nickname=player.nickname,
        birth_date=player.birth_date,
        email=player.email,
        password=player.password
    )
