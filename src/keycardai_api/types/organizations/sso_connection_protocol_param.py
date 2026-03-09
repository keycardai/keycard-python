# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SSOConnectionProtocolParam", "Oauth2", "Openid"]


class Oauth2(TypedDict, total=False):
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


class Openid(TypedDict, total=False):
    """OpenID Connect protocol configuration for SSO connection"""

    userinfo_endpoint: Optional[str]
    """OpenID Connect UserInfo endpoint"""


class SSOConnectionProtocolParam(TypedDict, total=False):
    """Protocol configuration for SSO connection"""

    oauth2: Optional[Oauth2]
    """OAuth 2.0 protocol configuration for SSO connection"""

    openid: Optional[Openid]
    """OpenID Connect protocol configuration for SSO connection"""
