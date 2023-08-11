from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from typing import Protocol

from db.enums import Gender


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
    main_lasso: int
    generic_square: GenericSquareDTO
    self_square: SelfSquareDTO


@dataclass(frozen=True, slots=True)
class CreateFateMatrixDTO:
    name: str
    gender: Gender
    date_of_birth: date
