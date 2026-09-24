# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PolicyVersion", "ArchivedByUser", "CreatedByUser"]


class ArchivedByUser(BaseModel):
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

    archived_by_user: Optional[ArchivedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """

    cedar_json: Optional[object] = None
    """Cedar policy in JSON representation.

    Populated by default and when `format=json` is passed; null when `format=cedar`
    narrows the response to the text representation only. Serialized verbatim from
    the stored Cedar so the order of `staticPolicies` matches the source policy
    order (ACC-613).
    """

    cedar_raw: Optional[str] = None
    """Cedar policy in human-readable syntax.

    Populated by default and when `format=cedar` is passed; null when `format=json`
    narrows the response to the JSON representation only.
    """

    created_by_user: Optional[CreatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """
