# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SSOConnectionRetrieveResponse", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class ProtocolsOauth2(BaseModel):
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


class ProtocolsOpenid(BaseModel):
    """OpenID Connect protocol configuration for SSO connection"""

    userinfo_endpoint: Optional[str] = None
    """OpenID Connect UserInfo endpoint"""


class Protocols(BaseModel):
    """Protocol configuration for SSO connection"""

    oauth2: Optional[ProtocolsOauth2] = None
    """OAuth 2.0 protocol configuration for SSO connection"""

    openid: Optional[ProtocolsOpenid] = None
    """OpenID Connect protocol configuration for SSO connection"""


class SSOConnectionRetrieveResponse(BaseModel):
    """SSO connection configuration for an organization"""

    id: str
    """Unique identifier for the SSO connection"""

    client_id: Optional[str] = None
    """OAuth 2.0 client ID"""

    client_secret_set: bool
    """Whether a client secret is configured"""

    created_at: datetime
    """The time the entity was created in utc"""

    identifier: str
    """SSO provider identifier (e.g., issuer URL)"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """

    protocols: Optional[Protocols] = None
    """Protocol configuration for SSO connection"""
