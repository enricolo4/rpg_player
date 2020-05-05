from falcon import Request, Response, json


class HealthController:
    def on_get(self, request: Request, response: Response):
        response.body = json.dumps({"status": "up"})
