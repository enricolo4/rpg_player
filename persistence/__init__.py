from sqlalchemy.orm import Session

from persistence.sql_alchemy_session import SQLAlchemySession

session: Session = SQLAlchemySession().session
