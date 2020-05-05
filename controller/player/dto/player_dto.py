from dataclasses import dataclass
from typing import Optional

from domain.model.player import Player


@dataclass
class PlayerDTO:
    name: str
    nickname: str
    birth_date: str
    email: str
    password: str
    test: Optional[str] = None

    @property
    def to_model(self) -> Player:
        return Player(
            name=self.name,
            nickname=self.nickname,
            birth_date=self.birth_date,
            email=self.email,
            password=self.password
        )


def to_dto(player: Player) -> PlayerDTO:
    return PlayerDTO(
        player.name,
        player.nickname,
        player.birth_date,
        player.email,
        player.password
    )


Player.to_dto = to_dto
