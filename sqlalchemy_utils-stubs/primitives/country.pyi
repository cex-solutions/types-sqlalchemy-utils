from __future__ import annotations

from typing import Union

from .. import i18n as i18n
from ..utils import str_coercible as str_coercible

@str_coercible
class Country:
    def __init__(self, code_or_country: Union[str, Country]) -> None:
        pass
    def name(self) -> str:
        pass
    @classmethod
    def validate(self, code: str) -> None:
        pass

