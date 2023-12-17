from typing import Protocol, TypeVar

_T = TypeVar("_T")


class DepencencyResolver(Protocol):
    async def __call__(self, dependency: type[_T]) -> _T:
        ...
