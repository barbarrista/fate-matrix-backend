from http import HTTPStatus
from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter
from result import Err

from app.core.domain.fate_matrix.commands import (
    CreateFateMatrixCommand,
)
from app.core.template_builder.builder import TemplateBuilder

from .schema import CreateFateMatrixSchema

router = APIRouter(prefix="/fate-matrix", tags=["fate-matrix"])


@router.post("", status_code=HTTPStatus.CREATED)
@inject
async def create_personal_fate_matrix(
    schema: CreateFateMatrixSchema,
    command: Annotated[CreateFateMatrixCommand, Inject],
    template_builder: Annotated[TemplateBuilder, Inject],
) -> str:
    result = await command.execute(dto=schema.to_dto())

    if isinstance(result, Err):
        raise NotImplementedError

    return template_builder.personal_fate_matrix(result.ok_value)
