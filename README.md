# 📝 Notes API

**Notes API** — это RESTful API на базе **FastAPI**, предназначенное для создания, хранения, редактирования и удаления заметок. Проект построен с использованием SQLAlchemy, Pydantic и SQLite.

---

## 🚀 Возможности

- 📄 Получение списка всех заметок
- 🔍 Получение заметки по ID
- ➕ Создание новой заметки
- ✏️ Полное и частичное обновление заметки
- ❌ Удаление заметки

---

## 📦 Используемые технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) — ASGI сервер

---

## ⚙️ Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/CASEYNGER/notes_api
cd notes_api
```

### 2. Создай и активируй виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Запусти сервер

```bash
uvicorn main:app --reload
```

