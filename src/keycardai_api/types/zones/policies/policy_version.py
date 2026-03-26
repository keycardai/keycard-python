# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PolicyVersion"]


class PolicyVersion(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    policy_id: str

    schema_version: str
    """Schema version this policy was validated against when created."""

    sha: str
    """Hex-encoded content hash"""

    version: int

    zone_id: str

    archived_at: Optional[datetime] = None

    archived_by: Optional[str] = None

    cedar_json: Optional[object] = None
    """Cedar policy in JSON representation. Populated when format=json (default)."""

    cedar_raw: Optional[str] = None
    """Cedar policy in human-readable syntax. Populated when format=cedar."""
