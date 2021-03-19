"""
Initialize databases script
"""
from db.db_base import metadata, engine


def init_db() -> None:
    """
    Initialize databases
    :return:
    """
    metadata.create_all(engine)
