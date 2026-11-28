# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .policy_set_manifest import PolicySetManifest

__all__ = ["PolicySetDraft", "UpdatedByUser", "Warning", "WarningDetail"]


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


class WarningDetail(BaseModel):
    """Additional structured context for a manifest warning.

    The shape depends on the warning type.
    """

    draft_schema_version: Optional[str] = None
    """Schema version the draft targets.

    Present only for schema_version_mismatch warnings.
    """

    policy_schema_version: Optional[str] = None
    """Schema version the policy version was validated against.

    Present only for schema_version_mismatch warnings.
    """


class Warning(BaseModel):
    message: str
    """Human-readable description of the warning, e.g.

    'validated against schema "2026-02-24", draft targets "2026-03-16"' or 'policy
    version is archived'.
    """

    policy_id: str

    policy_version_id: str

    type: Literal["policy_version_archived", "schema_version_mismatch"]

    detail: Optional[WarningDetail] = None
    """Additional structured context for a manifest warning.

    The shape depends on the warning type.
    """


class PolicySetDraft(BaseModel):
    created_at: datetime

    manifest: PolicySetManifest

    policy_set_id: str

    schema_version: str

    updated_at: datetime

    updated_by: str

    base_version_id: Optional[str] = None
    """ID of the policy set version this draft was hydrated from.

    Null when the draft was created without an existing version.
    """

    description: Optional[str] = None

    name: Optional[str] = None

    updated_by_user: Optional[UpdatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """

    warnings: Optional[List[Warning]] = None
    """
    Warnings about manifest entries that would prevent creating a version from this
    draft. Present only when there are warnings; omitted when empty.
    """
