from typing import TypeVar

from pydantic import BaseModel, ConfigDict


def _snake_to_camel(name: str) -> str:
    first, *rest = name.split("_")
    return first + "".join(map(str.capitalize, rest))


class BaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=_snake_to_camel, populate_by_name=True)


TSchema = TypeVar("TSchema", bound=BaseSchema)


class GenericSchema(BaseModel):
    model_config = ConfigDict(alias_generator=_snake_to_camel, populate_by_name=True)


class DescriptionSchema(BaseModel):
    description: str


class APIErrorSchema(BaseSchema):
    code: str
    message: str


class ObjectNotFoundAPIErrorSchema(APIErrorSchema):
    identifier: str


class RelationshipAPIErrorSchema(APIErrorSchema):
    identifier: str
    entity_name: str
