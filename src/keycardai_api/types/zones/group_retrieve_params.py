# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GroupRetrieveParams"]


class GroupRetrieveParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    expand: Annotated[
        Union[Literal["member_count", "roles"], List[Literal["member_count", "roles"]]], PropertyInfo(alias="expand[]")
    ]
