from core.domain.fate_matrix.dto import CreateFateMatrixDTO, PointsDTO
from core.domain.fate_matrix.service import FateMatrixCalculatorService
from result import Ok, Result


class CreateFateMatrixCommand:
    def __init__(self, service: FateMatrixCalculatorService) -> None:
        self._service = service

    async def execute(self, dto: CreateFateMatrixDTO) -> Result[PointsDTO, None]:
        first_square = self._service.calculate_first_diagonal_square(
            date_of_birth=dto.date_of_birth,
        )
        comfort_zone = self._service.get_comfort_zone(dto=first_square)
        third_square = self._service.calculate_third_diagonal_square(
            first_square=first_square,
            comfort_zone=comfort_zone,
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
        result = PointsDTO(
            a1=self_square.portrait.left,
            a2=self_square.portrait.middle,
            a3=self_square.portrait.right,
            b1=self_square.talents.top,
            b2=self_square.talents.middle,
            b3=self_square.talents.bottom,
            c1=self_square.material_karma.right,
            c2=self_square.material_karma.middle,
            c3=self_square.material_karma.left,
            d1=self_square.karmic_tail.bottom,
            d2=self_square.karmic_tail.middle,
            d3=self_square.karmic_tail.top,
            e=comfort_zone,
            i1=generic_square.bottom_left,
            i2=0,
            i3=0,
            f1=generic_square.top_left,
            f2=0,
            f3=0,
            g1=generic_square.top_right,
            g2=0,
            g3=0,
            h1=generic_square.bottom_right,
            h2=0,
            h3=0,
            h4=0,
            j1=0,
            j2=0,
            j3=0,
            k1=0,
            k2=0,
            l1=0,
            l2=0,
        )
        return Ok(result)
