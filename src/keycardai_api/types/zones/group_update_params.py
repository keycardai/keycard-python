# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    identifier: str
    """User-specified identifier, unique within the zone."""

    name: str
    """Human-readable group name"""
