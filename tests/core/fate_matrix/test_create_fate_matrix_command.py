import random
from collections.abc import Mapping
from datetime import date

import pytest
from faker import Faker
from result import Ok

from app.core.domain.fate_matrix.commands.create_fate_matrix import (
    CreateFateMatrixCommand,
)
from app.core.domain.fate_matrix.dto import CreateFateMatrixDTO, PointBundleDTO
from app.db.enums import Gender
from tests.abc_ import DepencencyResolver

pytestmark = pytest.mark.anyio


@pytest.fixture
async def command(
    dependency_resolver: DepencencyResolver,
) -> CreateFateMatrixCommand:
    return await dependency_resolver(CreateFateMatrixCommand)


@pytest.mark.parametrize(
    "date_of_birth",
    [
        date(1996, 4, 11),
        date(1998, 3, 11),
    ],
)
async def test_build_point_bundle(
    date_of_birth: date,
    faker: Faker,
    command: CreateFateMatrixCommand,
    point_bundle_mapping: Mapping[date, PointBundleDTO],
) -> None:
    result = command.execute(
        CreateFateMatrixDTO(
            name=faker.name(),
            gender=random.choice(list(Gender)),
            date_of_birth=date_of_birth,
        ),
    )
    assert isinstance(result, Ok)
    assert result.ok_value == point_bundle_mapping[date_of_birth]
