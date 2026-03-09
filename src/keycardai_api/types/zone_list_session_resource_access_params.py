# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ZoneListSessionResourceAccessParams"]


class ZoneListSessionResourceAccessParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    limit: int
    """Maximum number of items to return"""

    resource_id: str
    """Filter by resource ID"""

    rollup_children: bool
    """Include resource access from descendant sessions.

    When true (default), aggregates access from the session and all its descendants.
    When false, returns only direct access for the session.
    """

    session_id: str
    """Filter by session ID"""

    user_id: str
    """Filter by user ID"""
