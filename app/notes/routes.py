from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from .models import NoteModel
from .schemas import NoteCreate, NoteSchema, NoteUpdate
from .commons import get_note_or_404

notes_router = APIRouter(
    prefix='/notes', tags=['notes']
)


@notes_router.get(
        path='/',
        response_model=List[NoteSchema],
        summary='Получить все заметки',
        description='Возвращает список всех заметок из БД.',
        )
async def get_notes(db: Session = Depends(get_db)):
    """Получение всех заметок."""

    notes = db.query(NoteModel).all()
    return notes


@notes_router.post(
        path='/',
        response_model=NoteSchema,
        summary='Создать новую заметку',
        description='Создает новую заметку в БД.'
        )
async def add_note(
    note: NoteCreate,
    db: Session = Depends(get_db)
):
    """Создание новой заметки."""

    note_obj = NoteModel(**note.model_dump())
    db.add(note_obj)
    db.commit()
    db.refresh(note_obj)
    return note_obj


@notes_router.get(
        path='/{note_id}/',
        response_model=NoteSchema,
        summary='Получить заметку по id',
        description='Получает заметку из БД по ее id.'
        )
async def get_note(note_id: int, db: Session = Depends(get_db)):
    """Получение заметки по ее id."""

    note = get_note_or_404(db, note_id)
    return note


@notes_router.delete(
        path='/{note_id}/',
        response_model=NoteSchema,
        summary='Удалить заметку',
        description='Удаляет заметку из БД.'
    )
async def delete_note(note_id: int, db: Session = Depends(get_db)):
    """Удаление заметки."""

    note = get_note_or_404(db, note_id)
    db.delete(note)
    db.commit()

    return note


@notes_router.put(
        path='/{note_id}/',
        response_model=NoteSchema,
        summary='Обновить заметку',
        description='Обновляет полностью заметку в БД.'
        )
async def update_note(
    note_id: int,
    data: NoteCreate,
    db: Session = Depends(get_db)
):
    """Обновление заметки."""

    note = get_note_or_404(db, note_id)
    note.name = data.name
    note.description = data.description
    db.commit()
    db.refresh(note)

    return note


@notes_router.patch(
        path='/{note_id}/',
        response_model=NoteSchema,
        summary='Частично обновить заметку',
        description='Частично обновляет заметку в БД.'
        )
async def update_part_note(
    note_id: int,
    data: NoteUpdate,
    db: Session = Depends(get_db)
):
    """Частичное обновление заметки."""

    note = get_note_or_404(db, note_id)
    data_dict = data.model_dump(exclude_unset=True)

    for key, value in data_dict.items():
        setattr(note, key, value)

    db.commit()
    db.refresh(note)

    return note
