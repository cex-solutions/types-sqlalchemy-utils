from __future__ import annotations

from typing import Union

from .. import ImproperlyConfigured as ImproperlyConfigured, i18n as i18n
from ..utils import str_coercible as str_coercible

@str_coercible
class Currency:
    def __init__(self, code: Union[str, Currency]) -> None:
        pass
    @classmethod
    def validate(self, code: str) -> None:
        pass
    @property
    def symbol(self) -> str:
        pass
    @property
    def name(self) -> str:
        pass

