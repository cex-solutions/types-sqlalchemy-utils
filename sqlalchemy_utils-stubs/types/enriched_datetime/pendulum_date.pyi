from ...exceptions import ImproperlyConfigured as ImproperlyConfigured
from .pendulum_datetime import PendulumDateTime as PendulumDateTime
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
