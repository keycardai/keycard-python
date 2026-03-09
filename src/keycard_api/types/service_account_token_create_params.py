# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ServiceAccountTokenCreateParams"]


class ServiceAccountTokenCreateParams(TypedDict, total=False):
    client_id: Required[str]
    """Service account client ID"""

    client_secret: Required[str]
    """Service account client secret"""

    grant_type: Required[Literal["client_credentials"]]
    """OAuth 2.0 grant type (must be "client_credentials")"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
