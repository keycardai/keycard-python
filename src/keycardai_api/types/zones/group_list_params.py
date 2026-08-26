# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[
        Union[Literal["total_count", "member_count", "roles"], List[Literal["total_count", "member_count", "roles"]]],
        PropertyInfo(alias="expand[]"),
    ]

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to groups with this ID.

    Repeatable, max 100. Mutually exclusive with after/before.
    """

    filter_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[identifier]")]
    """Filter by exact group identifier"""

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """Search across name and identifier (substring match)"""

    sort: str
    """Comma-separated sort fields.

    Prefix with - for descending. Allowed: created_at, name, identifier
    """
