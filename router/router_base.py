from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# fastapi configuration
from db.db_base import database
from router.api.api import api_router


def get_router():
    app = FastAPI(title="REST API using FastAPI sqlite Async EndPoints")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # event configuration
    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    app.include_router(api_router)

    return app

