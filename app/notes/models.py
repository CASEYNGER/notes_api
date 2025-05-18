from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class NoteModel(Base):
    """Модель поста."""

    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(
        default=None, nullable=True
    )
    pub_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now()
    )
