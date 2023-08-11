from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter
from result import Err
from starlette import status

from core.domain.fate_matrix.commands.create_fate_matrix import CreateFateMatrixCommand

from .schema import CreateFateMatrixSchema, FateMatrixSchema

router = APIRouter(prefix="/fate-matrix", tags=["fate-matrix"])


@router.post(
    "",
    responses={
        status.HTTP_201_CREATED: {
            "model": FateMatrixSchema,
        },
    },
)
@inject
async def create_fate_matrix(
    schema: CreateFateMatrixSchema,
    command: Annotated[CreateFateMatrixCommand, Inject],
) -> FateMatrixSchema:
    dto = schema.to_dto()
    result = await command.execute(dto=dto)

    if isinstance(result, Err):
        match result:
            case _:
                raise NotImplementedError

    return FateMatrixSchema.from_dto(result.ok_value)
