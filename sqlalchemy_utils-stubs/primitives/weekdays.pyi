from collections.abc import Hashable
from collections.abc import Iterator

from ..utils import str_coercible as str_coercible
from .weekday import WeekDay as WeekDay

@str_coercible
class WeekDays:
    def __init__(self, bit_string_or_week_days: str | WeekDays | Hashable) -> None: ...
    def __iter__(self) -> Iterator[WeekDay]: ...
    def as_bit_string(self) -> str: ...
