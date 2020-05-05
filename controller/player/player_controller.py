import json

from falcon import Request, Response

from controller.player.dto.player_dto import PlayerDTO, player_to_dto
from domain.model.player import Player
from domain.service.player.player_service import PlayerService


class PlayerController:
    def __init__(self):
        self.__player_service = PlayerService()

    def on_post(self, request: Request, response: Response):
        player_dto = PlayerDTO(**request.media)

        player: Player = self.__player_service.save(player_dto.to_model)

        response.body = json.dumps(player_to_dto(player).__dict__)
