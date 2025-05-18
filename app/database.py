from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DB_URL = 'sqlite:///./notes.db'

engine = create_engine(DB_URL, echo=True)


class Base(DeclarativeBase):
    """Базовый класс для моделей."""
