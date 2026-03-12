# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ServiceAccountTokenCreateParams"]


class ServiceAccountTokenCreateParams(TypedDict, total=False):
    grant_type: Required[Literal["client_credentials"]]
    """OAuth 2.0 grant type (must be "client_credentials")"""

    client_id: Optional[str]
    """Service account client ID. Required if not using HTTP Basic Authentication."""

    client_secret: Optional[str]
    """Service account client secret. Required if not using HTTP Basic Authentication."""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
