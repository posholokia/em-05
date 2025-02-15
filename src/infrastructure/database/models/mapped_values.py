from datetime import datetime

from sqlalchemy import DateTime, CHAR, Date

from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated


datetime_tz = Annotated[datetime, mapped_column(DateTime(timezone=True))]
pkey = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
str1 = Annotated[str, mapped_column(CHAR(1))]
str3 = Annotated[str, mapped_column(CHAR(3))]
str4 = Annotated[str, mapped_column(CHAR(4))]
str11 = Annotated[str, mapped_column(CHAR(11))]
date = Annotated[datetime, mapped_column(Date())]
