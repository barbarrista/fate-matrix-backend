import aioinject

from core.domain.fate_matrix.commands.create_fate_matrix import CreateFateMatrixCommand
from core.domain.fate_matrix.service import FateMatrixCalculatorService

PROVIDERS = [
    aioinject.Callable(FateMatrixCalculatorService),
    aioinject.Callable(CreateFateMatrixCommand),
]
