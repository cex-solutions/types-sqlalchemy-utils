import sqlalchemy as sa
from typing import Any

has_postgres_json: bool

def __getattr__(name: str) -> Any: ...  # incomplete
