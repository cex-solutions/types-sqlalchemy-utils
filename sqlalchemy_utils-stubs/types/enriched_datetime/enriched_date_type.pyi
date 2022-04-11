from ..scalar_coercible import ScalarCoercible as ScalarCoercible
from .pendulum_date import PendulumDate as PendulumDate
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
