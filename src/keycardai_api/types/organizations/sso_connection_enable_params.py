# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sso_connection_protocol_param import SSOConnectionProtocolParam

__all__ = ["SSOConnectionEnableParams"]


class SSOConnectionEnableParams(TypedDict, total=False):
    client_id: Required[str]
    """OAuth 2.0 client ID"""

    identifier: Required[str]
    """SSO provider identifier (e.g., issuer URL)"""

    client_secret: str
    """OAuth 2.0 client secret (optional, will be encrypted if provided)"""

    protocols: Optional[SSOConnectionProtocolParam]
    """Protocol configuration for SSO connection"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
