from collections.abc import AsyncIterable

import aioinject
import dotenv
import httpx
import pytest
from fastapi import FastAPI

from core.di import create_container

dotenv.load_dotenv(".env")

pytest_plugins = [
    "anyio",
    "sqlalchemy_pytest.database",
    "tests.plugins.db",
]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
def fastapi_app() -> FastAPI:
    from adapters.api.app import create_app

    return create_app()


@pytest.fixture(scope="session")
def container() -> aioinject.Container:
    return create_container()


@pytest.fixture
async def http_client(
    fastapi_app: FastAPI,
) -> AsyncIterable[httpx.AsyncClient]:
    access_token = ""

    async with httpx.AsyncClient(
        app=fastapi_app,
        base_url="http://test",
        headers={"Authorization": f"Bearer {access_token}"},
    ) as client:
        yield client
