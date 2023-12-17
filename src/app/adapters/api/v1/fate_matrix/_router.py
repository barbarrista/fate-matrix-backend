from datetime import date
from http import HTTPStatus
from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
from result import Err

from app.core.domain.fate_matrix.commands import (
    CreateFateMatrixCommand,
)
from app.core.domain.fate_matrix.dto import CreateFateMatrixDTO
from app.core.template_builder.builder import TemplateBuilder
from app.db.enums import Gender

from .schema import CreateFateMatrixSchema

router = APIRouter(prefix="/fate-matrix", tags=["fate-matrix"])


@router.post("", status_code=HTTPStatus.CREATED)
@inject
async def create_personal_fate_matrix(
    schema: CreateFateMatrixSchema,
    command: Annotated[CreateFateMatrixCommand, Inject],
    template_builder: Annotated[TemplateBuilder, Inject],
) -> str:
    result = command.execute(dto=schema.to_dto())

    if isinstance(result, Err):
        raise NotImplementedError

    return template_builder.personal_fate_matrix(result.ok_value)


@router.get("")
@inject
async def build_personal_fate_matrix(
    date_of_birth: Annotated[date, Query(alias="dateOfBirth")],
    command: Annotated[CreateFateMatrixCommand, Inject],
    template_builder: Annotated[TemplateBuilder, Inject],
) -> HTMLResponse:
    result = command.execute(
        dto=CreateFateMatrixDTO(
            name="Name",
            date_of_birth=date_of_birth,
            gender=Gender.male,
        ),
    )

    if isinstance(result, Err):
        raise NotImplementedError

    svg = template_builder.personal_fate_matrix(result.ok_value)
    return HTMLResponse(content=svg)
