# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .zone_role import ZoneRole

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    role: Required[ZoneRole]
    """Zone role type.

    zone_manager has full management access, zone_viewer has read-only access.
    """
