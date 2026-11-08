# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ..policy_set_manifest import PolicySetManifest
from ..attestation_statement import AttestationStatement

__all__ = ["PolicySetVersion", "ArchivedByUser", "CreatedByUser"]


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


class PolicySetVersion(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    manifest: PolicySetManifest

    manifest_sha: str
    """Hex-encoded SHA-256 of the canonicalized manifest"""

    owner_type: Literal["platform", "customer"]
    """Who manages this policy set version:

    - `"platform"` — managed by the Keycard platform (system policy set versions).
    - `"customer"` — managed by the tenant (custom policy set versions).
    """

    policy_set_id: str

    schema_version: str
    """Schema version pinned to this policy set version.

    Determines the Cedar schema used for evaluation when activated.
    """

    version: int

    active: Optional[bool] = None
    """Whether this policy set version is currently bound with mode='active'.

    Always populated in responses; clients must treat absence as unknown rather than
    inferring 'not bound'.
    """

    archived_at: Optional[datetime] = None
    """Timestamp when the version was archived.

    Non-null only for archived versions; null or absent means not archived.
    """

    archived_by: Optional[str] = None
    """Identifier of the actor that archived the version.

    Null or absent means not archived.
    """

    archived_by_user: Optional[ArchivedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """

    attestation: Optional[AttestationStatement] = None
    """Decoded content of an Attestation JWS payload.

    Describes the exact policy set version composition at attestation time. This
    schema defines what consumers see after base64url-decoding the
    Attestation.payload field.
    """

    created_by_user: Optional[CreatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """
