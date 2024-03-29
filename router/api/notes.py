"""
Note api routes
"""
from typing import List

from fastapi import APIRouter
from starlette import status
from db.db_base import database
from entities.notes import notes
from dto.notes import NoteDto, NoteInDto

router = APIRouter()


@router.post("/", response_model=NoteDto, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteInDto):
    """
    create_note route
    :param note:
    :return:
    """
    query = notes.insert().values(text=note.text, completed=note.completed) # noqa
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


@router.put("/{note_id}/", response_model=NoteDto, status_code=status.HTTP_200_OK)
async def update_note(note_id: int, payload: NoteInDto):
    """
    update_note route
    :param note_id:
    :param payload:
    :return:
    """
    query = notes.update().where(notes.c.id == note_id).values(text=payload.text, completed=payload.completed) # noqa
    await database.execute(query)
    return {**payload.dict(), "id": note_id}


@router.get("/", response_model=List[NoteDto], status_code=status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    """
    read_notes route
    :param skip:
    :param take:
    :return:
    """
    query = notes.select().offset(skip).limit(take)
    return await database.fetch_all(query)


@router.get("/{note_id}/", response_model=NoteDto, status_code=status.HTTP_200_OK)
async def read_note(note_id: int):
    """
    read_note route
    :param note_id:
    :return:
    """
    query = notes.select().where(notes.c.id == note_id)
    return await database.fetch_one(query)


@router.delete("/{note_id}/", status_code=status.HTTP_200_OK)
async def delete_note(note_id: int):
    """
    delete_note route
    :param note_id:
    :return:
    """
    query = notes.delete().where(notes.c.id == note_id) # noqa
    await database.execute(query)
    return {"message": "Note with id: {} deleted successfully".format(note_id)}

