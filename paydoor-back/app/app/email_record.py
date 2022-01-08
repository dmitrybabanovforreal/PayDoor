from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class EmailRecord(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)