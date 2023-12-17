import aioinject

from app.core.template_builder import TemplateBuilder
from lib.di import Providers

PROVIDERS: Providers = [
    aioinject.Singleton(TemplateBuilder),
]
