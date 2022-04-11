from .functions import getdotattr as getdotattr
from .path import AttrPath as AttrPath
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
