from ..exceptions import ImproperlyConfigured as ImproperlyConfigured
from .scalar_coercible import ScalarCoercible as ScalarCoercible
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
