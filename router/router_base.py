"""
Base router
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.db_base import database
from router.api.api import api_router


def get_router():
    """
    Initialize router FastAPI
    :return:
    """
    app = FastAPI(title="REST API using FastAPI sqlite Async EndPoints")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def startup():  # pylint: disable=unused-variable
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():  # pylint: disable=unused-variable
        await database.disconnect()

    app.include_router(api_router)

    return app
