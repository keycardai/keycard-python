# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ZoneListParams"]


class ZoneListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    cursor: str

    expand: Annotated[
        Union[Literal["total_count", "permissions"], List[Literal["total_count", "permissions"]]],
        PropertyInfo(alias="expand[]"),
    ]

    limit: int
    """Maximum number of items to return"""

    slug: str
