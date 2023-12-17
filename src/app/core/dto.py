from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel

_T = TypeVar("_T")


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True


class PaginationDTO(BaseDTO):
    page: int
    page_size: int


@dataclass(frozen=True, slots=True)
class PaginationResultDTO(Generic[_T]):
    items: Sequence[_T]
    has_next_page: bool
    count: int
