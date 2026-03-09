# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zone_role import ZoneRole

__all__ = ["MemberAddParams"]


class MemberAddParams(TypedDict, total=False):
    organization_user_id: Required[str]
    """Organization user ID to add to the zone"""

    role: Required[ZoneRole]
    """Zone role type.

    zone_manager has full management access, zone_viewer has read-only access.
    """
