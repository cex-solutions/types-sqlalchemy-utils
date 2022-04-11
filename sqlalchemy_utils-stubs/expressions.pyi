from .functions.orm import quote as quote
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
