from datetime import datetime

from core.utils import utc_now
from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(default=utc_now)


class TimeMixin(CreatedAtMixin):
    updated_at: Mapped[datetime] = mapped_column(default=utc_now, onupdate=utc_now)
