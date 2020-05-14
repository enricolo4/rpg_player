from falcon import Request, Response
from sqlalchemy.orm import scoping

from persistence import session


class SQLAlchemySessionManager:
    def __init__(self):
        self.__session = session
        self.__scoped = isinstance(self.__session, scoping.ScopedSession)

    def process_request(self, req: Request, resp: Response):
        """
        Handle post-processing of the response (after routing).
        """
        req.context['session'] = self.__session

    def process_response(self, req: Request, resp: Response, resource, req_succeeded):
        """
        Handle post-processing of the response (after routing).
        """
        session_context = req.context['session']

        session_context.commit()

        if self.__scoped:
            print("Removing Context")
            session_context.remove()
        else:
            print("Closing Context")
            session_context.close()
