# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    active: Literal["true"]

    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    limit: int
    """Maximum number of items to return"""

    session_type: Literal["user", "application"]

    status: Literal["active", "expired", "revoked"]

    user_id: str
    """Filter by user ID"""
