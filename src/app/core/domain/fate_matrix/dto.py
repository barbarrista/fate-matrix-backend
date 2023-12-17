from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from typing import Protocol

from app.db.enums import Gender


class AsSequenceProtocol(Protocol):
    def as_tuple(self) -> Sequence[int]:
        ...


@dataclass(frozen=True, slots=True)
class GenericSquareDTO:
    bottom_left: int
    top_left: int
    top_right: int
    bottom_right: int


@dataclass(frozen=True, slots=True)
class PortraitLassoDTO(AsSequenceProtocol):
    right: int
    middle: int
    left: int

    def as_tuple(self) -> Sequence[int]:
        return (self.right, self.middle, self.left)


@dataclass(frozen=True, slots=True)
class TalentsLassoDTO(AsSequenceProtocol):
    bottom: int
    middle: int
    top: int

    def as_tuple(self) -> Sequence[int]:
        return (self.bottom, self.middle, self.top)


@dataclass(frozen=True, slots=True)
class MaterialKarmaLassoDTO(AsSequenceProtocol):
    left: int
    middle: int
    right: int

    def as_tuple(self) -> Sequence[int]:
        return (self.left, self.middle, self.right)


@dataclass(frozen=True, slots=True)
class KarmicTailLassoDTO(AsSequenceProtocol):
    top: int
    middle: int
    bottom: int

    def as_tuple(self) -> Sequence[int]:
        return (self.top, self.middle, self.bottom)


@dataclass(frozen=True, slots=True)
class SelfSquareDTO:
    portrait: PortraitLassoDTO
    talents: TalentsLassoDTO
    material_karma: MaterialKarmaLassoDTO
    karmic_tail: KarmicTailLassoDTO


@dataclass(frozen=True, slots=True)
class DiagonalSquareVerticeDTO:
    left: int
    top: int
    right: int
    bottom: int


@dataclass(frozen=True, slots=True)
class FateMatrixDTO:
    comfort_zone: int
    generic_square: GenericSquareDTO
    self_square: SelfSquareDTO


@dataclass(frozen=True, slots=True)
class CreateFateMatrixDTO:
    name: str
    gender: Gender
    date_of_birth: date


@dataclass(frozen=True, slots=True)
class PointsDTO:
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
