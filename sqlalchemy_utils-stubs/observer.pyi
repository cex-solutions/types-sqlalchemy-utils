from .functions import getdotattr as getdotattr, has_changes as has_changes
from .path import AttrPath as AttrPath
from .utils import is_sequence as is_sequence
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
