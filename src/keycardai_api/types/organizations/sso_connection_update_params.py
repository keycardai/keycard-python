# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
    """Protocol configuration for an SSO connection update.

    Omit a protocol to leave it unchanged.
    """

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for an SSO connection update.

    Each field is tri-state, omit to leave unchanged, send null to clear, send a value to set.
    """

    authorization_endpoint: Optional[str]
    """OAuth 2.0 authorization endpoint. Set to null to clear."""

    authorization_parameters: Optional[Dict[str, str]]
    """Custom query parameters appended to authorization redirect URLs.

    Use for non-standard providers (e.g. Google prompt=consent,
    access_type=offline). Set to null to clear.
    """

    code_challenge_methods_supported: Optional[SequenceNotStr[str]]
    """Supported PKCE code challenge methods. Set to null to clear."""

    jwks_uri: Optional[str]
    """JSON Web Key Set endpoint. Set to null to clear."""

    registration_endpoint: Optional[str]
    """OAuth 2.0 registration endpoint. Set to null to clear."""

    scopes_supported: Optional[SequenceNotStr[str]]
    """Supported OAuth 2.0 scopes. Set to null to clear."""

    token_endpoint: Optional[str]
    """OAuth 2.0 token endpoint. Set to null to clear."""


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration for an SSO connection update.

    Each field is tri-state, omit to leave unchanged, send null to clear, send a value to set.
    """

    scopes: Optional[SequenceNotStr[str]]
    """Additional OIDC scopes to request from this provider during authentication (e.g.

    "groups"). Merged with the default scopes (openid, profile, email). Set to null
    to clear.
    """

    user_identifier_claim: Optional[str]
    """
    Name of a top-level string claim in the provider's ID Token to use as the user
    identifier on user creation. Set to null to clear.
    """

    userinfo_endpoint: Optional[str]
    """OpenID Connect UserInfo endpoint. Set to null to clear."""


class Protocols(TypedDict, total=False):
    """Protocol configuration for an SSO connection update.

    Omit a protocol to leave it unchanged.
    """

    oauth2: Optional[ProtocolsOauth2]
    """OAuth 2.0 protocol configuration for an SSO connection update.

    Each field is tri-state, omit to leave unchanged, send null to clear, send a
    value to set.
    """

    openid: Optional[ProtocolsOpenid]
    """OpenID Connect protocol configuration for an SSO connection update.

    Each field is tri-state, omit to leave unchanged, send null to clear, send a
    value to set.
    """
