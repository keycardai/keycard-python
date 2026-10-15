# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
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

    filter_organization_id: Annotated[str, PropertyInfo(alias="filter[organization_id]")]

    filter_permission_in: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[permission][in]")]
    """
    Only return zones where the caller is allowed ANY of these permissions
    (`<resource_type>:<action>`, e.g. `applications:list`). Repeatable (one
    permission per occurrence); values are unioned, max 20 (a stricter cap than the
    authorization service's 50). The accessible zone set is resolved by the
    authorization service and composes with cursor pagination, search, sort and
    `expand[]=total_count`. Malformed values are a 400.
    """

    limit: int
    """Maximum number of items to return"""

    slug: str
