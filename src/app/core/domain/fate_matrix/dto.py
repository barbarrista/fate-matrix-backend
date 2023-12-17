from dataclasses import dataclass
from datetime import date

from app.db.enums import Gender


@dataclass(frozen=True, slots=True)
class CreateFateMatrixDTO:
    name: str
    gender: Gender
    date_of_birth: date


@dataclass(frozen=True, slots=True)
class FirstRankPersonalPointsDTO:
    a1: int
    b1: int
    c1: int
    d1: int


@dataclass(frozen=True, slots=True)
class SecondRankPersonalPointsDTO:
    a2: int
    b2: int
    c2: int
    d2: int


@dataclass(frozen=True, slots=True)
class ThirdRankPersonalPointsDTO:
    a3: int
    b3: int
    c3: int
    d3: int


@dataclass(frozen=True, slots=True)
class FirstRankGenericPointsDTO:
    f1: int
    g1: int
    h1: int
    i1: int


@dataclass(frozen=True, slots=True)
class SecondRankGenericPointsDTO:
    i2: int
    f2: int
    g2: int
    h2: int


@dataclass(frozen=True, slots=True)
class ThirdRankGenericPointsDTO:
    i3: int
    f3: int
    g3: int
    h3: int


@dataclass(frozen=True, slots=True)
class LoveAndMoneyPointsDTO:
    j1: int
    j2: int
    j3: int


@dataclass(frozen=True, slots=True)
class SupportPointsDTO:
    l1: int
    l2: int


@dataclass(frozen=True, slots=True)
class PointBundleDTO:
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
