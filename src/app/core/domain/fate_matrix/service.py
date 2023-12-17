from datetime import date

from app.core.domain.fate_matrix.dto import (
    DiagonalSquareVerticeDTO,
    GenericSquareDTO,
    KarmicTailLassoDTO,
    MaterialKarmaLassoDTO,
    PortraitLassoDTO,
    SelfSquareDTO,
    TalentsLassoDTO,
)


class FateMatrixCalculatorService:
    max_archetypes_count = 22

    def calculate_first_diagonal_square(
        self,
        date_of_birth: date,
    ) -> DiagonalSquareVerticeDTO:
        left = self.sum_of_number(date_of_birth.day)
        top = date_of_birth.month
        right = self.sum_of_number(date_of_birth.year)
        bottom = self.sum_of_number(left + top + right)
        return DiagonalSquareVerticeDTO(
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    def calculate_second_diagonal_square(
        self,
        first_square: DiagonalSquareVerticeDTO,
        third_square: DiagonalSquareVerticeDTO,
    ) -> DiagonalSquareVerticeDTO:
        left = self.sum_of_number(first_square.left + third_square.left)
        top = self.sum_of_number(first_square.top + third_square.top)
        right = self.sum_of_number(first_square.right + third_square.right)
        bottom = self.sum_of_number(first_square.bottom + third_square.bottom)
        return DiagonalSquareVerticeDTO(
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    def calculate_third_diagonal_square(
        self,
        first_square: DiagonalSquareVerticeDTO,
        comfort_zone: int,
    ) -> DiagonalSquareVerticeDTO:
        left = self.sum_of_number(first_square.left + comfort_zone)
        top = self.sum_of_number(first_square.top + comfort_zone)
        right = self.sum_of_number(first_square.right + comfort_zone)
        bottom = self.sum_of_number(first_square.bottom + comfort_zone)
        return DiagonalSquareVerticeDTO(
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    def get_comfort_zone(self, dto: DiagonalSquareVerticeDTO) -> int:
        return self.sum_of_number(number=dto.left + dto.top + dto.right + dto.bottom)

    def calculate_generic_square(
        self,
        dto: DiagonalSquareVerticeDTO,
    ) -> GenericSquareDTO:
        bottom_left = self.sum_of_number(dto.bottom + dto.left)
        top_left = self.sum_of_number(dto.left + dto.top)
        top_right = self.sum_of_number(dto.top + dto.right)
        bottom_right = self.sum_of_number(dto.bottom + dto.right)
        return GenericSquareDTO(
            bottom_left=bottom_left,
            top_left=top_left,
            top_right=top_right,
            bottom_right=bottom_right,
        )

    @staticmethod
    def get_build_self_square(
        first_square: DiagonalSquareVerticeDTO,
        second_square: DiagonalSquareVerticeDTO,
        third_square: DiagonalSquareVerticeDTO,
    ) -> SelfSquareDTO:
        portrait = PortraitLassoDTO(
            left=first_square.left,
            middle=second_square.left,
            right=third_square.left,
        )
        talents = TalentsLassoDTO(
            top=first_square.top,
            middle=second_square.top,
            bottom=third_square.top,
        )
        material_karma = MaterialKarmaLassoDTO(
            left=third_square.right,
            middle=second_square.right,
            right=first_square.right,
        )
        karmic_tail = KarmicTailLassoDTO(
            bottom=first_square.bottom,
            middle=second_square.bottom,
            top=third_square.bottom,
        )
        return SelfSquareDTO(
            portrait=portrait,
            talents=talents,
            material_karma=material_karma,
            karmic_tail=karmic_tail,
        )

    def sum_of_number(self, number: int) -> int:
        if number <= self.max_archetypes_count:
            return number

        sum_ = 0
        while number != 0:
            sum_ = sum_ + (number % 10)
            number = number // 10

        if sum_ > self.max_archetypes_count:
            return self.sum_of_number(number=sum_)

        return sum_
