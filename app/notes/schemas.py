from datetime import datetime
from typing import Union, Optional

from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    description: Union[str, None] = None


class NoteUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class NoteSchema(NoteCreate):
    id: int
    pub_date: datetime

    model_config = ConfigDict(from_attributes=True)
