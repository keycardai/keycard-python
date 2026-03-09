# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ZoneRetrieveParams"]


class ZoneRetrieveParams(TypedDict, total=False):
    expand: Annotated[Union[Literal["permissions"], List[Literal["permissions"]]], PropertyInfo(alias="expand[]")]
