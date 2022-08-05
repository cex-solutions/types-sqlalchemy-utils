from __future__ import annotations

from typing import Hashable, Generator, Union

from ..utils import str_coercible as str_coercible
from .weekday import WeekDay as WeekDay


@str_coercible
class WeekDays:
    def __init__(self, bit_string_or_week_days: Union[str, WeekDays, Hashable]) -> None:
        pass

    def __iter__(self) -> Generator[WeekDay, None, None]:
        pass

    def as_bit_string(self) -> str:
        pass