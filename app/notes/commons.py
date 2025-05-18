from fastapi import HTTPException

from sqlalchemy.orm import Session

from .models import NoteModel


def get_note_or_404(db: Session, note_id: int) -> NoteModel:
    """Получение заметки по id."""

    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(
            status_code=404,
            detail='Note not found.'
        )
    return note
