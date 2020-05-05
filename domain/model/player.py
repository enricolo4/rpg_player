from typing import Optional
from uuid import UUID
from dataclasses import dataclass


@dataclass
class Player:
    name: str
    nickname: str
    birth_date: str
    email: str
    password: str
    id: Optional[UUID] = None
