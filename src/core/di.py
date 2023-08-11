import functools
from collections.abc import Iterable

import aioinject

from db.dependencies import create_session
from settings import AppSettings, get_settings


def _register_all(
    container: aioinject.Container,
    providers: Iterable[aioinject.Provider],
) -> None:
    for provider in providers:
        container.register(provider)


@functools.lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()
    container.register(aioinject.Callable(create_session))

    for settings_cls in (AppSettings,):
        container.register(
            aioinject.Object(get_settings(settings_cls), type_=settings_cls),
        )

    return container
