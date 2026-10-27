# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PolicySet", "CreatedByUser", "UpdatedByUser"]


class CreatedByUser(BaseModel):
    """The organization user behind a `created_by`, `updated_by` or `archived_by` value.

    Returned only when `expand[]=user` is requested.
    """

    id: str
    """Public ID of the user in the organization's platform zone.

    This is not the same value as the `*_by` field it expands; use it to link to
    `/zones/{zone_id}/users/{id}`.
    """

    email: Optional[str] = None
    """The user's email address, or null when not known."""

    zone_id: str
    """Public ID of the organization's platform zone the user belongs to."""


class UpdatedByUser(BaseModel):
    """The organization user behind a `created_by`, `updated_by` or `archived_by` value.

    Returned only when `expand[]=user` is requested.
    """

    id: str
    """Public ID of the user in the organization's platform zone.

    This is not the same value as the `*_by` field it expands; use it to link to
    `/zones/{zone_id}/users/{id}`.
    """

    email: Optional[str] = None
    """The user's email address, or null when not known."""

    zone_id: str
    """Public ID of the organization's platform zone the user belongs to."""


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

    created_by_user: Optional[CreatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """

    latest_version: Optional[int] = None
    """Human-readable version number of the latest version (e.g., 1, 2, 3)"""

    latest_version_id: Optional[str] = None

    updated_by: Optional[str] = None

    updated_by_user: Optional[UpdatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """
