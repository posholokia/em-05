from sqlalchemy.orm import DeclarativeBase, Mapped

from infrastructure.database.models.mapped_values import pkey


class BaseModel(DeclarativeBase):
    id: Mapped[pkey]
