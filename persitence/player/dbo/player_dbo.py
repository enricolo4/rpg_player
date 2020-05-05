import uuid
from uuid import UUID
from dataclasses import dataclass

from domain.model.player import Player


@dataclass
class PlayerDBO:
    id: UUID
    name: str
    nickname: str
    birth_date: str
    email: str
    password: str

    def to_model(self) -> Player:
        return Player(
            id=self.id,
            name=self.name,
            nickname=self.nickname,
            birth_date=self.birth_date,
            email=self.email,
            password=self.password
        )


def to_dbo(player: Player) -> PlayerDBO:
    return PlayerDBO(
        id=uuid.uuid4(),
        name=player.name,
        nickname=player.nickname,
        birth_date=player.birth_date,
        email=player.email,
        password=player.password
    )


Player.to_dbo = to_dbo
