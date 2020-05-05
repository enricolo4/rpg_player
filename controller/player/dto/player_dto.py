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
    id: Optional[str] = None

    @property
    def to_model(self) -> Player:
        return Player(
            name=self.name,
            nickname=self.nickname,
            birth_date=self.birth_date,
            email=self.email,
            password=self.password
        )


def player_to_dto(player: Player) -> PlayerDTO:
    return PlayerDTO(
        id=str(player.id),
        name=player.name,
        nickname=player.nickname,
        birth_date=player.birth_date,
        email=player.email,
        password=player.password
    )
