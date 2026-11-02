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
            Literal[
                "total_count",
                "session_count",
                "grant_count",
                "role-assignments",
                "groups",
                "credentials",
                "credentials.provider",
            ],
            List[
                Literal[
                    "total_count",
                    "session_count",
                    "grant_count",
                    "role-assignments",
                    "groups",
                    "credentials",
                    "credentials.provider",
                ]
            ],
        ],
        PropertyInfo(alias="expand[]"),
    ]

    filter_email: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[email]")]
    """Filter by exact email address"""

    filter_external: Annotated[bool, PropertyInfo(alias="filter[external]")]
    """
    Filter by source: `false` for users managed in Keycard, `true` for users
    provisioned by an external directory. Omit to list both.
    """

    filter_groups: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[groups]")]
    """Restrict to members of this group (by group ID).

    Repeatable; OR'd across values.
    """

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to users with this publicId.

    Repeatable, max 100. Mutually exclusive with after/before.
    """

    filter_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[identifier]")]
    """Filter by exact user identifier"""

    filter_issuer: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[issuer]")]
    """Filter by exact `issuer`. Repeatable; OR'd across values."""

    filter_role: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[role]")]
    """Restrict to users directly granted this role (by role identifier).

    Repeatable, max 100; OR'd across values. Group-inherited grants do not match.
    """

    filter_subject: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[subject]")]
    """Filter by exact `subject`. Repeatable; OR'd across values."""

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """Search across email and the user's `subject` (substring match)"""

    query_email: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[email]")]
    """Search by email (substring match)"""

    query_subject: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[subject]")]
    """Search by the user's `subject` (substring match)"""

    role_source: Literal["user", "group", "all"]
    """
    Selects which grants `expand[]=role-assignments` returns, tagging each with
    `source`: `user` (direct only, the default), `group` (group-inherited only), or
    `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.
    """

    sort: str
    """Comma-separated sort fields.

    Prefix with - for descending. Allowed: created_at, email, authenticated_at
    """
