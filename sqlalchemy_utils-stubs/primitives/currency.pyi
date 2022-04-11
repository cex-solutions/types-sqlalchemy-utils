from .. import ImproperlyConfigured as ImproperlyConfigured, i18n as i18n
from ..utils import str_coercible as str_coercible
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
