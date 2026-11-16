# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResourceRetrieveParams"]


class ResourceRetrieveParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    expand: Annotated[
        Union[Literal["credential_provider"], List[Literal["credential_provider"]]], PropertyInfo(alias="expand[]")
    ]
