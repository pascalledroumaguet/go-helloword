"""
DTO Configuration
"""
from pydantic import BaseModel


class NoteInDto(BaseModel):
    """
    NoteInDto
    """
    text: str
    completed: bool


class NoteDto(BaseModel):
    """
    NoteDto
    """
    id: int
    text: str
    completed: bool
