from collections.abc import Mapping
from datetime import date

import pytest

from app.core.domain.fate_matrix.dto import PointBundleDTO
from app.core.domain.fate_matrix.service import FateMatrixCalculatorService
from tests.abc_ import DepencencyResolver

pytestmark = pytest.mark.anyio


@pytest.fixture
async def service(
    dependency_resolver: DepencencyResolver,
) -> FateMatrixCalculatorService:
    return await dependency_resolver(FateMatrixCalculatorService)


@pytest.mark.parametrize(
    "date_of_birth",
    [
        date(1996, 4, 11),
        date(1998, 3, 11),
    ],
)
async def test_build_point_bundle(
    date_of_birth: date,
    service: FateMatrixCalculatorService,
    point_bundle_mapping: Mapping[date, PointBundleDTO],
) -> None:
    point_bundle = service.build_point_bundle(date_of_birth)
    assert point_bundle == point_bundle_mapping[date_of_birth]
