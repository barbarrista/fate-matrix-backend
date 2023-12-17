from collections.abc import AsyncIterable, AsyncIterator
from typing import TypeVar, cast

import aioinject
import dotenv
import httpx
import pytest
from faker import Faker
from fastapi import FastAPI

from app.di import create_container
from tests.abc_ import DepencencyResolver

_T = TypeVar("_T")

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
    from app.adapters.api.app import create_app

    return create_app()


@pytest.fixture(scope="session")
def container() -> aioinject.Container:
    return create_container()


@pytest.fixture
def faker() -> Faker:
    return Faker(locale="ru_RU")


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


@pytest.fixture
async def aioinject_context(
    container: aioinject.Container,
) -> AsyncIterator[aioinject.InjectionContext]:
    async with container.context() as ctx:
        yield ctx


@pytest.fixture
async def dependency_resolver(
    aioinject_context: aioinject.InjectionContext,
) -> DepencencyResolver:
    async def resolver(dependency: type[_T]) -> _T:
        return cast(_T, await aioinject_context.resolve(dependency))

    return resolver
