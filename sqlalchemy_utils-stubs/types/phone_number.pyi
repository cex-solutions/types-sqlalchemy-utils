from ..exceptions import ImproperlyConfigured as ImproperlyConfigured
from ..utils import str_coercible as str_coercible
from .scalar_coercible import ScalarCoercible as ScalarCoercible
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
