# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SchemaVersion"]


class SchemaVersion(BaseModel):
    created_at: datetime

    status: Literal["active", "deprecated", "archived"]

    updated_at: datetime

    version: str

    archived_at: Optional[datetime] = None

    cedar_schema: Optional[str] = None
    """Cedar schema in human-readable syntax. Populated when format=cedar."""

    cedar_schema_json: Optional[object] = None
    """Cedar schema as JSON object. Populated when format=json (default)."""

    deprecated_at: Optional[datetime] = None
