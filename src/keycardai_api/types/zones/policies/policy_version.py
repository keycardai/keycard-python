# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PolicyVersion"]


class PolicyVersion(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    owner_type: Literal["platform", "customer"]
    """Who manages this policy version:

    - `"platform"` — managed by the Keycard platform (system policy versions).
    - `"customer"` — managed by the tenant (custom policy versions).
    """

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
    """Cedar policy in JSON representation.

    Populated by default and when `format=json` is passed; null when `format=cedar`
    narrows the response to the text representation only.
    """

    cedar_raw: Optional[str] = None
    """Cedar policy in human-readable syntax.

    Populated by default and when `format=cedar` is passed; null when `format=json`
    narrows the response to the JSON representation only.
    """
