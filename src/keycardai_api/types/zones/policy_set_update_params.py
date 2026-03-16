# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySetUpdateParams"]


class PolicySetUpdateParams(TypedDict, total=False):
    zone_id: Required[str]

    name: str

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
