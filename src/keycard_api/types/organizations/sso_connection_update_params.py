# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .sso_connection_protocol_param import SSOConnectionProtocolParam

__all__ = ["SSOConnectionUpdateParams"]


class SSOConnectionUpdateParams(TypedDict, total=False):
    client_id: str
    """OAuth 2.0 client ID (set to null to remove)"""

    client_secret: str
    """OAuth 2.0 client secret (set to null to remove)"""

    identifier: str
    """SSO provider identifier (e.g., issuer URL)"""

    protocols: Optional[SSOConnectionProtocolParam]
    """Protocol configuration for SSO connection"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
