from datetime import date
from typing import Self

from adapters.api.schema import BaseSchema
from core.domain.fate_matrix.dto import (
    CreateFateMatrixDTO,
    FateMatrixDTO,
    GenericSquareDTO,
    SelfSquareDTO,
)
from db.enums import Gender


class CreateFateMatrixSchema(BaseSchema):
    name: str
    gender: Gender
    date_of_birth: date

    def to_dto(self) -> CreateFateMatrixDTO:
        return CreateFateMatrixDTO(
            name=self.name,
            gender=self.gender,
            date_of_birth=self.date_of_birth,
        )


class GenericSquareSchema(BaseSchema):
    bottom_left: int
    top_left: int
    top_right: int
    bottom_right: int

    @classmethod
    def from_dto(cls, dto: GenericSquareDTO) -> Self:
        return cls(
            bottom_left=dto.bottom_left,
            top_left=dto.top_left,
            top_right=dto.top_right,
            bottom_right=dto.bottom_right,
        )


class SelfSquareSchema(BaseSchema):
    portrait: tuple[int, int, int]
    talents: tuple[int, int, int]
    material_karma: tuple[int, int, int]
    karmic_tail: tuple[int, int, int]

    @classmethod
    def from_dto(cls, dto: SelfSquareDTO) -> Self:
        return cls(
            portrait=dto.portrait.as_tuple(),
            talents=dto.talents.as_tuple(),
            material_karma=dto.material_karma.as_tuple(),
            karmic_tail=dto.karmic_tail.as_tuple(),
        )


class FateMatrixSchema(BaseSchema):
    main_lasso: int
    generic_square: GenericSquareSchema
    self_square: SelfSquareSchema

    @classmethod
    def from_dto(cls, dto: FateMatrixDTO) -> Self:
        return cls(
            main_lasso=dto.main_lasso,
            generic_square=GenericSquareSchema.from_dto(dto.generic_square),
            self_square=SelfSquareSchema.from_dto(dto.self_square),
        )
