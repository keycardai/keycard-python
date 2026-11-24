# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PolicyDraft", "UpdatedByUser"]


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


class PolicyDraft(BaseModel):
    created_at: datetime

    policy_id: str

    schema_version: str

    updated_at: datetime

    updated_by: str

    base_version_id: Optional[str] = None
    """ID of the policy version this draft was hydrated from.

    Null when the draft was created without an existing version.
    """

    cedar_json: Optional[object] = None
    """Cedar policy in JSON representation.

    Populated by default and when `format=json` is passed; null when `format=cedar`
    narrows the response to the text representation only. Serialized verbatim from
    the converted Cedar so the order of `staticPolicies` matches the source policy
    order (ACC-613).
    """

    cedar_raw: Optional[str] = None
    """Cedar policy in human-readable syntax.

    Populated by default and when `format=cedar` is passed; null when `format=json`
    narrows the response to the JSON representation only.
    """

    updated_by_user: Optional[UpdatedByUser] = None
    """The organization user behind a `created_by`, `updated_by` or `archived_by`
    value.

    Returned only when `expand[]=user` is requested.
    """
