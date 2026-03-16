# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .policy_set import PolicySet

__all__ = ["PolicySetWithBinding"]


class PolicySetWithBinding(PolicySet):
    active: Optional[bool] = None
    """Whether this policy set is currently bound to a scope"""

    active_version: Optional[int] = None
    """Human-readable version number of the active version (e.g., 1, 2, 3)"""

    active_version_id: Optional[str] = None
    """Public ID of the currently active (bound) version"""

    mode: Optional[Literal["active", "shadow"]] = None

    scope_target_id: Optional[str] = None
