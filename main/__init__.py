import falcon
from waitress import serve

from controller.health.health_controller import HealthController
from controller.player.player_controller import PlayerController
from main.middleware.sql_alchemy_session_manager import SQLAlchemySessionManager

application = falcon.API(middleware=[SQLAlchemySessionManager()])

application.add_route("/health", HealthController())
application.add_route("/player", PlayerController())

if __name__ == '__main__':
    serve(app=application, host="127.0.0.1", port=5555)
