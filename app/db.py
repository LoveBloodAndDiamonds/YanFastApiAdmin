import datetime

from sqlalchemy import Column, Date, String, Integer
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from app.config import Config

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    # Уникальный айди ключа
    id = Column(Integer, primary_key=True)

    # Имя пользователя
    username = Column(String, unique=True)

    # Дата истечения подписки
    expired_date = Column(Date, default=datetime.date.today() + datetime.timedelta(days=90))

    def __str__(self):
        return f"[{self.id}]: {self.username}, {self.expired_date}"


# Инициализация базы данных
engine: Engine = create_engine(Config.DATABASE_URL)
session_maker: sessionmaker[Session] = sessionmaker(engine)
Base.metadata.create_all(engine)
