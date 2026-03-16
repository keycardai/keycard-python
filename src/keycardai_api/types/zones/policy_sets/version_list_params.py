# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    zone_id: Required[str]

    after: str
    """Return items after this cursor (forward pagination).

    Use after_cursor from a previous response. Mutually exclusive with before.
    """

    before: str
    """Return items before this cursor (backward pagination).

    Use before_cursor from a previous response. Mutually exclusive with after.
    """

    expand: List[Literal["total_count"]]
    """Opt-in to additional response fields"""

    limit: int
    """Maximum number of items to return"""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
