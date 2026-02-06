# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SSOConnectionUpdateParams", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class SSOConnectionUpdateParams(TypedDict, total=False):
    client_id: str
    """OAuth 2.0 client ID (set to null to remove)"""

    client_secret: str
    """OAuth 2.0 client secret (set to null to remove)"""

    identifier: str
    """SSO provider identifier (e.g., issuer URL)"""

    protocols: Optional[Protocols]
    """Protocol configuration for SSO connection"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for SSO connection"""

    authorization_endpoint: Optional[str]
    """OAuth 2.0 authorization endpoint"""

    code_challenge_methods_supported: Optional[SequenceNotStr[str]]
    """Supported PKCE code challenge methods"""

    jwks_uri: Optional[str]
    """JSON Web Key Set endpoint"""

    registration_endpoint: Optional[str]
    """OAuth 2.0 registration endpoint"""

    scopes_supported: Optional[SequenceNotStr[str]]
    """Supported OAuth 2.0 scopes"""

    token_endpoint: Optional[str]
    """OAuth 2.0 token endpoint"""


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration for SSO connection"""

    userinfo_endpoint: Optional[str]
    """OpenID Connect UserInfo endpoint"""


class Protocols(TypedDict, total=False):
    """Protocol configuration for SSO connection"""

    oauth2: Optional[ProtocolsOauth2]
    """OAuth 2.0 protocol configuration for SSO connection"""

    openid: Optional[ProtocolsOpenid]
    """OpenID Connect protocol configuration for SSO connection"""
