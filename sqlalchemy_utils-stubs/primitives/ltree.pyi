from __future__ import annotations

import re
from typing import Union, List, Optional

from ..utils import str_coercible as str_coercible


path_matcher: re.Pattern


@str_coercible
class Ltree:
    def __init__(self, path_or_ltree: Union[str, Ltree]) -> None:
        pass

    @classmethod
    def validate(cls, path: str) -> None:
        pass

    def index(self, other: Union[str, Ltree]) -> int:
        pass

    def descendant_of(self, other: Union[str, Ltree]) -> bool:
        pass

    def ancestor_of(self, other: Union[str, Ltree]) -> bool:
        pass

    def __getitem__(self, key: Union[int, slice]) -> Ltree:
        pass

    def lca(self, *others: List[Union[str, Ltree]]) -> Optional[Ltree]:
        pass

    def __add__(self, other: Union[str, Ltree]) -> Ltree:
        pass

    def __radd__(self, other: Union[str, Ltree]) -> Ltree:
        pass