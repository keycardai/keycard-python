# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationListCredentialsParams"]


class ApplicationListCredentialsParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    cursor: str

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    limit: int
    """Maximum number of items to return"""
