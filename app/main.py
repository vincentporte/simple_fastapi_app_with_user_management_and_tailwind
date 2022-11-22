from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings
from app.views import commodity_views


def get_application() -> FastAPI:

    app = FastAPI(docs_url="/", title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "localhost"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    app.include_router(commodity_views, prefix="/commodities", tags=["Commodities"])

    return app


app = get_application()


@app.get("/healthcheck")
async def status():
    return {"status": "up"}
