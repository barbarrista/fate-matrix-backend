import aioinject

from app.core.domain.fate_matrix.commands.create_fate_matrix import (
    CreateFateMatrixCommand,
)
from app.core.domain.fate_matrix.service import FateMatrixCalculatorService
from lib.di import Providers

PROVIDERS: Providers = [
    aioinject.Callable(FateMatrixCalculatorService),
    aioinject.Callable(CreateFateMatrixCommand),
]
