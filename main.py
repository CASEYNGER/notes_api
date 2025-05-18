from fastapi import FastAPI

from app.database import Base, engine
from app.notes.routes import notes_router

app = FastAPI(
    title='NoteAPI',
    description='Простое API для управления заметками.',
    version='0.1.0',
    contact={
        'name': 'CASEYNGER',
        'email': 'iam@caseynger.ru',
        'url': 'https://github.com/CASEYNGER'
    },
    license_info={
        'name': 'MIT License',
    },
    docs_url='/docs',
    redoc_url='/redoc'
)

Base.metadata.create_all(bind=engine)

app.include_router(notes_router)
