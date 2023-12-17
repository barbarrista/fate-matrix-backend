from datetime import date

from app.core.domain.fate_matrix.dto import (
    FirstRankGenericPointsDTO,
    FirstRankPersonalPointsDTO,
    LoveAndMoneyPointsDTO,
    PointBundleDTO,
    SecondRankGenericPointsDTO,
    SecondRankPersonalPointsDTO,
    SupportPointsDTO,
    ThirdRankGenericPointsDTO,
    ThirdRankPersonalPointsDTO,
)
from app.core.utils import sum_of_number


class FateMatrixCalculatorService:
    def get_first_rank_personal_points(
        self,
        date_of_birth: date,
    ) -> FirstRankPersonalPointsDTO:
        a1 = sum_of_number(date_of_birth.day)
        b1 = date_of_birth.month
        c1 = sum_of_number(date_of_birth.year)
        d1 = sum_of_number(a1 + b1 + c1)
        return FirstRankPersonalPointsDTO(a1=a1, b1=b1, c1=c1, d1=d1)

    def get_second_rank_personal_points(
        self,
        first_rank_dto: FirstRankPersonalPointsDTO,
        third_rank_dto: ThirdRankPersonalPointsDTO,
    ) -> SecondRankPersonalPointsDTO:
        return SecondRankPersonalPointsDTO(
            a2=sum_of_number(first_rank_dto.a1 + third_rank_dto.a3),
            b2=sum_of_number(first_rank_dto.b1 + third_rank_dto.b3),
            c2=sum_of_number(first_rank_dto.c1 + third_rank_dto.c3),
            d2=sum_of_number(first_rank_dto.d1 + third_rank_dto.d3),
        )

    def get_third_rank_personal_points(
        self,
        dto: FirstRankPersonalPointsDTO,
        comfort_zone: int,
    ) -> ThirdRankPersonalPointsDTO:
        return ThirdRankPersonalPointsDTO(
            a3=sum_of_number(dto.a1 + comfort_zone),
            b3=sum_of_number(dto.b1 + comfort_zone),
            c3=sum_of_number(dto.c1 + comfort_zone),
            d3=sum_of_number(dto.d1 + comfort_zone),
        )

    def get_first_rank_generic_points(
        self,
        dto: FirstRankPersonalPointsDTO,
    ) -> FirstRankGenericPointsDTO:
        return FirstRankGenericPointsDTO(
            i1=sum_of_number(dto.d1 + dto.a1),
            f1=sum_of_number(dto.b1 + dto.c1),
            g1=sum_of_number(dto.a1 + dto.b1),
            h1=sum_of_number(dto.d1 + dto.c1),
        )

    def get_second_rank_generic_points(
        self,
        first_rank_dto: FirstRankGenericPointsDTO,
        third_rank_dto: ThirdRankGenericPointsDTO,
    ) -> SecondRankGenericPointsDTO:
        return SecondRankGenericPointsDTO(
            i2=sum_of_number(first_rank_dto.i1 + third_rank_dto.i3),
            g2=sum_of_number(first_rank_dto.g1 + third_rank_dto.g3),
            f2=sum_of_number(first_rank_dto.f1 + third_rank_dto.f3),
            h2=sum_of_number(first_rank_dto.h1 + third_rank_dto.h3),
        )

    def get_third_rank_generic_points(
        self,
        dto: FirstRankGenericPointsDTO,
        comfort_zone: int,
    ) -> ThirdRankGenericPointsDTO:
        return ThirdRankGenericPointsDTO(
            i3=sum_of_number(dto.i1 + comfort_zone),
            g3=sum_of_number(dto.g1 + comfort_zone),
            f3=sum_of_number(dto.f1 + comfort_zone),
            h3=sum_of_number(dto.h1 + comfort_zone),
        )

    def get_love_and_money_points(self, d3: int, c3: int) -> LoveAndMoneyPointsDTO:
        j2 = sum_of_number(d3 + c3)
        j1 = sum_of_number(d3 + j2)
        j3 = sum_of_number(c3 + j2)
        return LoveAndMoneyPointsDTO(
            j1=j1,
            j2=j2,
            j3=j3,
        )

    def get_support_points(
        self,
        a3: int,
        b3: int,
        comfort_zone: int,
    ) -> SupportPointsDTO:
        return SupportPointsDTO(
            l1=sum_of_number(a3 + comfort_zone),
            l2=sum_of_number(b3 + comfort_zone),
        )

    def get_comfort_zone(self, dto: FirstRankPersonalPointsDTO) -> int:
        return sum_of_number(dto.a1 + dto.b1 + dto.c1 + dto.d1)

    def build_point_bundle(self, date_of_birth: date) -> PointBundleDTO:
        first_rank_personal_dto = self.get_first_rank_personal_points(date_of_birth)
        comfort_zone = self.get_comfort_zone(first_rank_personal_dto)
        third_rank_personal_dto = self.get_third_rank_personal_points(
            dto=first_rank_personal_dto,
            comfort_zone=comfort_zone,
        )
        second_rank_personal_dto = self.get_second_rank_personal_points(
            first_rank_dto=first_rank_personal_dto,
            third_rank_dto=third_rank_personal_dto,
        )

        first_rank_generic_dto = self.get_first_rank_generic_points(
            first_rank_personal_dto,
        )
        third_rank_generic_dto = self.get_third_rank_generic_points(
            dto=first_rank_generic_dto,
            comfort_zone=comfort_zone,
        )
        second_rank_generic_dto = self.get_second_rank_generic_points(
            first_rank_dto=first_rank_generic_dto,
            third_rank_dto=third_rank_generic_dto,
        )
        love_and_money_points = self.get_love_and_money_points(
            d3=third_rank_personal_dto.d3,
            c3=third_rank_personal_dto.c3,
        )
        support_points = self.get_support_points(
            a3=third_rank_personal_dto.d3,
            b3=third_rank_personal_dto.c3,
            comfort_zone=comfort_zone,
        )

        k1 = sum_of_number(third_rank_personal_dto.a3 + third_rank_personal_dto.c3)
        k2 = sum_of_number(comfort_zone + k1)
        h4 = sum_of_number(second_rank_personal_dto.c2 + second_rank_personal_dto.d2)

        return PointBundleDTO(
            a1=first_rank_personal_dto.a1,
            b1=first_rank_personal_dto.b1,
            c1=first_rank_personal_dto.c1,
            d1=first_rank_personal_dto.d1,
            a2=second_rank_personal_dto.a2,
            b2=second_rank_personal_dto.b2,
            c2=second_rank_personal_dto.c2,
            d2=second_rank_personal_dto.d2,
            a3=third_rank_personal_dto.a3,
            b3=third_rank_personal_dto.b3,
            c3=third_rank_personal_dto.c3,
            d3=third_rank_personal_dto.d3,
            e=comfort_zone,
            i1=first_rank_generic_dto.i1,
            g1=first_rank_generic_dto.g1,
            f1=first_rank_generic_dto.f1,
            h1=first_rank_generic_dto.h1,
            i2=second_rank_generic_dto.i2,
            g2=second_rank_generic_dto.g2,
            f2=second_rank_generic_dto.f2,
            h2=second_rank_generic_dto.h2,
            i3=third_rank_generic_dto.i3,
            g3=third_rank_generic_dto.g3,
            f3=third_rank_generic_dto.f3,
            h3=third_rank_generic_dto.h3,
            h4=h4,
            j1=love_and_money_points.j1,
            j2=love_and_money_points.j2,
            j3=love_and_money_points.j3,
            l1=support_points.l1,
            l2=support_points.l2,
            k1=k1,
            k2=k2,
        )
