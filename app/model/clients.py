from pydantic import BaseModel


class BaseClient(BaseModel):
    id: int
    name: str
    email: str
    address: str
    cep: str
    birthdate: str
    phone: str

    class Config:
        from_attributes = True
        validate_assignment = True


""" from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DbClient(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, unique=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    cep = Column(String)
    birthdate = Column(Date)
    phone = Column(String)
 """
