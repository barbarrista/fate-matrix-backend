import httpx
import pytest
from fastapi import FastAPI

pytestmark = [pytest.mark.anyio]


async def test_healthcheck(
    fastapi_app: FastAPI,
    http_client: httpx.AsyncClient,
) -> None:
    url = fastapi_app.url_path_for("healthcheck")
    response = await http_client.get(url)
    assert response.status_code == httpx.codes.OK
