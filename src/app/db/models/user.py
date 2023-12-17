from db.base import Base, str_64, str_128, str_320, uuid_pk
from db.mixins import TimeMixin
from sqlalchemy import false, true
from sqlalchemy.orm import Mapped, mapped_column


class User(TimeMixin, Base):
    __tablename__ = "user"

    id: Mapped[uuid_pk]
    first_name: Mapped[str_128 | None]
    last_name: Mapped[str_128 | None]
    middle_name: Mapped[str_128 | None]
    email: Mapped[str_320] = mapped_column(unique=True)
    password_hash: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True, server_default=true())
    is_confirmed: Mapped[bool] = mapped_column(default=False, server_default=false())
    username: Mapped[str_64] = mapped_column(unique=True)
