from .. import i18n as i18n
from ..exceptions import ImproperlyConfigured as ImproperlyConfigured
from ..primitives import WeekDay as WeekDay, WeekDays as WeekDays
from .bit import BitType as BitType
from .scalar_coercible import ScalarCoercible as ScalarCoercible
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
