from dataclasses import asdict
from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter
from result import Err
from starlette import status

from app.core.domain.fate_matrix.commands.create_fate_matrix import (
    CreateFateMatrixCommand,
)

from .schema import CreateFateMatrixSchema, FateMatrixSchema, PointsSchema

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
) -> PointsSchema:
    result = await command.execute(dto=schema.to_dto())

    if isinstance(result, Err):
        raise NotImplementedError

    return PointsSchema.model_validate(asdict(result.ok_value))
