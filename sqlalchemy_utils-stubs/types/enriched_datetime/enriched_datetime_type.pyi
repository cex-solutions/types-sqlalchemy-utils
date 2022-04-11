from ..scalar_coercible import ScalarCoercible as ScalarCoercible
from .pendulum_datetime import PendulumDateTime as PendulumDateTime
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
