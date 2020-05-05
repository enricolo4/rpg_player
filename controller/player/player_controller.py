import json

from falcon import Request, Response

from controller.player.dto.player_dto import PlayerDTO
from domain.model.player import Player
from domain.service.player.player_service import PlayerService


# PlayerDTO(
#     name=request.media["name"],
#     nickname=request.media["nickname"],
#     birth_date=request.media["birth_date"],
#     email=request.media["email"],
#     password=request.media["password"]
# )


class PlayerController:
    def __init__(self):
        self.__player_service = PlayerService()

    def on_post(self, request: Request, response: Response):
        player_dto = PlayerDTO(**request.media)

        player: Player = self.__player_service.save(player_dto.to_model)

        response.body = json.dumps(player.to_dto().__dict__)
