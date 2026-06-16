# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PolicySet"]


class PolicySet(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    owner_type: Literal["platform", "customer"]
    """Who manages this policy set:

    - `"platform"` — managed by the Keycard platform (system policies).
    - `"customer"` — managed by the tenant (custom policies).
    """

    scope_type: Literal["zone", "resource", "user", "session"]
    """**Deprecated.** Use `target_type` instead. Carries the same value."""

    target_type: Literal["zone", "user"]
    """What this policy set targets:

    - `"zone"` — applies to all requests in the zone.
    - `"user"` — scoped to a specific user.

    `resource` and `session` are reserved; legacy sets with those scopes carry them
    in the deprecated `scope_type` field.
    """

    updated_at: datetime

    zone_id: str

    archived_at: Optional[datetime] = None

    latest_version: Optional[int] = None
    """Human-readable version number of the latest version (e.g., 1, 2, 3)"""

    latest_version_id: Optional[str] = None

    updated_by: Optional[str] = None
