import falcon
from waitress import serve

from controller.health.health_controller import HealthController
from controller.player.player_controller import PlayerController

app = falcon.API()

app.add_route("/health", HealthController())
app.add_route("/player", PlayerController())

if __name__ == '__main__':
    serve(app=app, host="127.0.0.1", port=5555)
