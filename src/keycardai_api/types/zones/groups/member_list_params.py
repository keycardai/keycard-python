# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[
        Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]], PropertyInfo(alias="expand[]")
    ]

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to the member with this user ID.

    Repeatable, max 100. Mutually exclusive with after/before.
    """

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """
    Search members by their user's email or federated credential subject (substring
    match)
    """
