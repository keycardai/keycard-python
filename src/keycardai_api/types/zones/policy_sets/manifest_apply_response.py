# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .policy_set_version import PolicySetVersion
from ..policy_set_binding import PolicySetBinding

__all__ = ["ManifestApplyResponse", "Change", "Warning"]


class Change(BaseModel):
    action: Literal["created_policy", "created_version", "reused", "repinned", "dropped"]
    """
    `repinned`: an explicit `policy_version_id` replaced a different version the set
    already pinned for that policy; no version minted.
    """

    name: str
    """The policy's name.

    Lets a caller correlate a `created_policy` row with its `new_policy` request
    entry without a re-list.
    """

    policy_id: str

    policy_version_id: Optional[str] = None
    """Absent when action is dropped."""


class Warning(BaseModel):
    code: str
    """Machine-readable warning code, e.g. unknown_actions."""

    message: str


class ManifestApplyResponse(BaseModel):
    changes: List[Change]
    """Per-policy outcome of the diff."""

    created: bool
    """True when the server mints a new policy set version.

    False when the content matches the latest version, even when activate changes
    the active binding. Reverts to older content mint a new version at the tip and
    return true.
    """

    binding: Optional[PolicySetBinding] = None
    """Present when activate was true."""

    policy_set_version: Optional[PolicySetVersion] = None
    """The resulting version. Omitted on dry_run."""

    warnings: Optional[List[Warning]] = None
    """Non-fatal findings — e.g.

    Cedar actions unknown to the resolved schema. Present only when non-empty.
    """
