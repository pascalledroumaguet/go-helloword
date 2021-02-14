from db.db_base import metadata, engine


def init_db() -> None:
    metadata.create_all(engine)
