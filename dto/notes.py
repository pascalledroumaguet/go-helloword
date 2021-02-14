# DTO Configuration
from pydantic import BaseModel


class NoteInDto(BaseModel):
    text: str
    completed: bool


class NoteDto(BaseModel):
    id: int
    text: str
    completed: bool
