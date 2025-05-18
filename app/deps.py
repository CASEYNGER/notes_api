from sqlalchemy.orm import sessionmaker

from app.database import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    Предоставляет объект SQLAlchemy-сессии в каждом запросе
    и автоматически закрывает соединение после его завершения.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
