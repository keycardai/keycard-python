# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    limit: int
    """Maximum number of members to return"""

    role: Literal["zone_manager", "zone_viewer"]
    """Filter members by role"""
