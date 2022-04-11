from ..primitives import Country as Country
from .scalar_coercible import ScalarCoercible as ScalarCoercible
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
