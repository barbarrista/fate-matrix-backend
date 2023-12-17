from result import Ok, Result

from app.core.domain.fate_matrix.dto import CreateFateMatrixDTO, PointBundleDTO
from app.core.domain.fate_matrix.service import FateMatrixCalculatorService


class CreateFateMatrixCommand:
    def __init__(self, service: FateMatrixCalculatorService) -> None:
        self._service = service

    def execute(self, dto: CreateFateMatrixDTO) -> Result[PointBundleDTO, None]:
        result = self._service.build_point_bundle(dto.date_of_birth)
        return Ok(result)
