from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings
from app.routes import commodity_routes


def my_schema():
    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "description": "Simple FastAPI App with User Management, Tailwind CSS, Dockerized Postgres and Poetry",
        "contact": {
            "name": "Get Help with this API",
            "url": "https://github.com/vincentporte/simple_fastapi_app_with_user_management_and_tailwind",
            "email": "contact@neuralia.co",
        },
        "license": {
            "name": "License : MIT",
            "url": "https://github.com/vincentporte/simple_fastapi_app_with_user_management_and_tailwind/blob/main/LICENSE",
        },
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def get_application() -> FastAPI:

    app = FastAPI(docs_url="/", title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.openapi = my_schema

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
    app.include_router(commodity_routes, prefix="/commodities", tags=["Commodities"])

    return app


app = get_application()


@app.get("/healthcheck")
async def status():
    return {"status": "up"}
