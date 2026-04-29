# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Policy"]


class Policy(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    owner_type: Literal["platform", "customer"]
    """Who manages this policy:

    - `"platform"` — managed by the Keycard platform (system policies).
    - `"customer"` — managed by the tenant (custom policies).
    """

    updated_at: datetime

    zone_id: str

    archived_at: Optional[datetime] = None

    description: Optional[str] = None

    latest_schema_version: Optional[str] = None
    """Schema version the latest version was validated against (e.g., "2026-02-24").

    Null when the policy has no published versions. Denormalized from
    `PolicyVersion.schema_version` for the policy referenced by `latest_version_id`.
    """

    latest_version: Optional[int] = None
    """Human-readable version number of the latest version (e.g., 1, 2, 3)"""

    latest_version_id: Optional[str] = None

    updated_by: Optional[str] = None
