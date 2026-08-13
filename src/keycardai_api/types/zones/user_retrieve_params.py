# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveParams"]


class UserRetrieveParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    expand: Annotated[
        Union[Literal["role-assignments", "groups"], List[Literal["role-assignments", "groups"]]],
        PropertyInfo(alias="expand[]"),
    ]

    role_source: Literal["user", "group", "all"]
    """
    Selects which grants `expand[]=role-assignments` returns, tagging each with
    `source`: `user` (direct only, the default), `group` (group-inherited only), or
    `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.
    """
