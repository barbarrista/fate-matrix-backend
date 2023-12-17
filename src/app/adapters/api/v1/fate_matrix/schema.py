from datetime import date

from app.adapters.api.schema import BaseSchema
from app.core.domain.fate_matrix.dto import (
    CreateFateMatrixDTO,
)
from app.db.enums import Gender


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


class PointsSchema(BaseSchema):
    a1: int
    a2: int
    a3: int

    b1: int
    b2: int
    b3: int

    c1: int
    c2: int
    c3: int

    d1: int
    d2: int
    d3: int

    e: int

    f1: int
    f2: int
    f3: int

    g1: int
    g2: int
    g3: int

    h1: int
    h2: int
    h3: int
    h4: int

    i1: int
    i2: int
    i3: int

    j1: int
    j2: int
    j3: int

    k1: int
    k2: int

    l1: int
    l2: int
