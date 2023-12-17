import functools
import itertools
from collections.abc import Iterable

import aioinject
from pydantic_settings import BaseSettings

from app.db.dependencies import create_session
from app.settings import AppSettings, get_settings
from lib.di import Providers

from .modules import fate_matrix, template_builder

MODULES: Iterable[Providers] = (
    fate_matrix.PROVIDERS,
    template_builder.PROVIDERS,
)

SETTINGS: Iterable[type[BaseSettings]] = (AppSettings,)


def _register_providers(
    container: aioinject.Container,
) -> None:
    for provider in itertools.chain.from_iterable(MODULES):
        container.register(provider)


def _register_settings(container: aioinject.Container) -> None:
    for settings_cls in SETTINGS:
        container.register(
            aioinject.Object(get_settings(settings_cls), type_=settings_cls),
        )


@functools.lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()
    container.register(aioinject.Callable(create_session))

    _register_providers(container)
    _register_settings(container)

    return container
