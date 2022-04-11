from typing import Any

from ..primitives import Ltree as Ltree
from .scalar_coercible import ScalarCoercible as ScalarCoercible

def __getattr__(name: str) -> Any: ...  # incomplete
