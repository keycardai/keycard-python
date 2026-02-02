# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ServiceAccountCreateParams"]


class ServiceAccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """Service account name"""

    description: str
    """Optional description of the service account"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]

    x_request_id: Annotated[str, PropertyInfo(alias="X-Request-ID")]
