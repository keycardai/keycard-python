# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PolicySetBinding"]


class PolicySetBinding(BaseModel):
    id: str
    """Binding identifier (stable per slot)"""

    created_at: datetime

    mode: Literal["active", "shadow"]
    """Binding mode"""

    policy_set_id: str
    """Public ID of the bound policy set"""

    policy_set_version_id: str
    """Public ID of the bound policy set version"""

    scope_target_id: str
    """**Deprecated.** Use `target_id` instead. Carries the same value."""

    scope_type: Literal["zone"]
    """**Deprecated.** Use `target_type` instead. Carries the same value."""

    target_id: str
    """Target entity ID. Equals zone_id for zone-targeted bindings."""

    target_type: Literal["zone", "user"]
    """What this binding targets"""
