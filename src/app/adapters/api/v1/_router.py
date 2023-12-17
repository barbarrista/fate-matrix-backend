from fastapi import APIRouter

from . import fate_matrix

router = APIRouter(prefix="/api/v1", tags=["v1"])
router.include_router(fate_matrix.router)
