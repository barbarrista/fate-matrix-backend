import contextlib
from collections.abc import AsyncIterator
from contextlib import aclosing

from aioinject.ext.fastapi import InjectMiddleware
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import sentry
from core.di import create_container
from settings import AppSettings, get_settings

from .middleware import CommitSessionMiddleware


@contextlib.asynccontextmanager
async def _lifespan(
    app: FastAPI,  # noqa: ARG001 - required by lifespan protocol
) -> AsyncIterator[None]:
    async with aclosing(create_container()):
        yield


def create_app() -> FastAPI:
    sentry.init_sentry()

    app = FastAPI(lifespan=_lifespan)

    _include_routers(app=app)
    _add_exception_handlers(app=app)
    _add_middlewares(app=app)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    return app


def _include_routers(app: FastAPI) -> None:  # noqa: ARG001
    pass


def _add_exception_handlers(app: FastAPI) -> None:  # noqa: ARG001
    pass


def _add_middlewares(app: FastAPI) -> None:
    app_settings = get_settings(AppSettings)

    app.add_middleware(CommitSessionMiddleware)
    app.add_middleware(InjectMiddleware, container=create_container())
    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.allow_origins,
        allow_origin_regex=app_settings.allow_origin_regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
