# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Policy", "CreatedByUser", "UpdatedByUser"]


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

    created_by_user: Optional[CreatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """

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

    updated_by_user: Optional[UpdatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """
