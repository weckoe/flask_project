from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password_1 = Column(String(100))
    password_2 = Column(String(100))

    def __init__(self, username=None, password_1=None, password_2=None):
        self.username = username
        self.password_2 = password_2
        self.password_1 = password_1
