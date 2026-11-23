# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RoleListParams"]


class RoleListParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    filter_scope_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[scope_id]")]
    """Restrict results to assignments scoped to this target ID (e.g.

    a zone ID). Repeatable, max 100; values are OR'd. Unscoped assignments never
    match.
    """

    filter_scoped: Annotated[bool, PropertyInfo(alias="filter[scoped]")]
    """`false` keeps only unscoped assignments (those applying to the zone itself, e.g.

    an org role); `true` keeps only scoped ones. Omit to list both.
    """

    limit: int
    """Maximum number of items to return"""
