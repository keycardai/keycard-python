# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .policy_set import PolicySet
from .policy_set_binding import PolicySetBinding
from .policy_sets.policy_set_version import PolicySetVersion

__all__ = ["PolicySetWithBinding", "PolicySetWithBindingChange", "PolicySetWithBindingWarning"]


class PolicySetWithBindingChange(BaseModel):
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


class PolicySetWithBindingWarning(BaseModel):
    code: str
    """Machine-readable warning code, e.g. unknown_actions."""

    message: str


class PolicySetWithBinding(PolicySet):
    active: Optional[bool] = None
    """Whether this policy set is currently bound to a scope"""

    active_version: Optional[int] = None
    """Human-readable version number of the active version (e.g., 1, 2, 3)"""

    active_version_id: Optional[str] = None
    """Public ID of the currently active (bound) version"""

    binding: Optional[PolicySetBinding] = None
    """Active zone binding, present when created with `manifest.activate` set to true."""

    changes: Optional[List[PolicySetWithBindingChange]] = None
    """Per-policy outcomes, present only when created with a manifest."""

    mode: Optional[Literal["active", "shadow"]] = None

    policy_set_version: Optional[PolicySetVersion] = None
    """First version, present only when created with a manifest."""

    scope_target_id: Optional[str] = None
    """**Deprecated.** Use `target_id` instead.

    Carries the active binding's target; null when unbound.
    """

    shadow_version: Optional[int] = None
    """Human-readable version number of the shadow version"""

    shadow_version_id: Optional[str] = None
    """Public ID of the shadow (observed) version, if any"""

    target_id: Optional[str] = None
    """Target entity ID.

    Equals `zone_id` for zone-targeted sets; the principal identifier for
    principal-scoped sets. Null only for legacy non-zone sets that predate target
    tracking.
    """

    warnings: Optional[List[PolicySetWithBindingWarning]] = None
    """Non-fatal findings, present only when non-empty on create."""
