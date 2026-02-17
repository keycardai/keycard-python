# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ZoneListSessionResourceAccessParams"]


class ZoneListSessionResourceAccessParams(TypedDict, total=False):
    resource_id: str
    """Filter by resource ID"""

    session_id: str
    """Filter by session ID"""

    user_id: str
    """Filter by user ID"""
