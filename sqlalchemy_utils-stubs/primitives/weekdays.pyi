from typing import Any

from ..utils import str_coercible as str_coercible
from .weekday import WeekDay as WeekDay

def __getattr__(name: str) -> Any: ...  # incomplete
