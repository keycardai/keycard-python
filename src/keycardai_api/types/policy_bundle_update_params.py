# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PolicyBundleUpdateParams"]


class PolicyBundleUpdateParams(TypedDict, total=False):
    if_match: Annotated[str, PropertyInfo(alias="If-Match")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
