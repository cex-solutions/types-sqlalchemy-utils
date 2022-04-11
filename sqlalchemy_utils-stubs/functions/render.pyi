from .mock import create_mock_engine as create_mock_engine
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
