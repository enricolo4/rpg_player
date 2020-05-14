import uuid

from sqlalchemy import Column, DateTime, func, String
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class BaseDBO:
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    FIELD = {}
