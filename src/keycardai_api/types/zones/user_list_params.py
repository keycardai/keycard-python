# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[
        Union[
            Literal["total_count", "session_count", "grant_count", "role-assignments"],
            List[Literal["total_count", "session_count", "grant_count", "role-assignments"]],
        ],
        PropertyInfo(alias="expand[]"),
    ]

    filter_email: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[email]")]
    """Filter by exact email address"""

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to users with this publicId.

    Repeatable, max 100. Mutually exclusive with after/before.
    """

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """Search across email and credential subject (substring match)"""

    query_email: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[email]")]
    """Search by email (substring match)"""

    query_subject: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[subject]")]
    """Search by federated credential subject (substring match)"""

    sort: str
    """Comma-separated sort fields.

    Prefix with - for descending. Allowed: created_at, email, authenticated_at
    """
