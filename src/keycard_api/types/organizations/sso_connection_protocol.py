# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SSOConnectionProtocol", "Oauth2", "Openid"]


class Oauth2(BaseModel):
    """OAuth 2.0 protocol configuration for SSO connection"""

    authorization_endpoint: Optional[str] = None
    """OAuth 2.0 authorization endpoint"""

    code_challenge_methods_supported: Optional[List[str]] = None
    """Supported PKCE code challenge methods"""

    jwks_uri: Optional[str] = None
    """JSON Web Key Set endpoint"""

    registration_endpoint: Optional[str] = None
    """OAuth 2.0 registration endpoint"""

    scopes_supported: Optional[List[str]] = None
    """Supported OAuth 2.0 scopes"""

    token_endpoint: Optional[str] = None
    """OAuth 2.0 token endpoint"""


class Openid(BaseModel):
    """OpenID Connect protocol configuration for SSO connection"""

    userinfo_endpoint: Optional[str] = None
    """OpenID Connect UserInfo endpoint"""


class SSOConnectionProtocol(BaseModel):
    """Protocol configuration for SSO connection"""

    oauth2: Optional[Oauth2] = None
    """OAuth 2.0 protocol configuration for SSO connection"""

    openid: Optional[Openid] = None
    """OpenID Connect protocol configuration for SSO connection"""
