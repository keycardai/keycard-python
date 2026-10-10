# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionRetrieveParams"]


class VersionRetrieveParams(TypedDict, total=False):
    zone_id: Required[str]

    policy_set_id: Required[str]

    expand: List[Literal["user"]]
    """Opt-in to additional response fields on a single resource (`user`). Repeatable."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
