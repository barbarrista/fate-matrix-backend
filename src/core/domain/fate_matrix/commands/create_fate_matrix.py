from result import Ok, Result

from core.domain.fate_matrix.dto import CreateFateMatrixDTO, FateMatrixDTO
from core.domain.fate_matrix.service import FateMatrixCalculatorService


class CreateFateMatrixCommand:
    def __init__(self, service: FateMatrixCalculatorService) -> None:
        self._service = service

    async def execute(self, dto: CreateFateMatrixDTO) -> Result[FateMatrixDTO, None]:
        first_square = self._service.calculate_first_diagonal_square(
            date_of_birth=dto.date_of_birth,
        )
        main_lasso = self._service.calculate_main_lasso(dto=first_square)
        third_square = self._service.calculate_third_diagonal_square(
            first_square=first_square,
            main_lasso=main_lasso,
        )
        second_square = self._service.calculate_second_diagonal_square(
            first_square=first_square,
            third_square=third_square,
        )

        generic_square = self._service.calculate_generic_square(dto=first_square)

        self_square = self._service.get_build_self_square(
            first_square=first_square,
            second_square=second_square,
            third_square=third_square,
        )

        result = FateMatrixDTO(
            main_lasso=main_lasso,
            generic_square=generic_square,
            self_square=self_square,
        )
        return Ok(result)
