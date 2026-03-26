# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ProviderCreateParams", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class ProviderCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """User specified identifier, unique within the zone"""

    name: Required[str]
    """Human-readable name"""

    client_id: str
    """OAuth 2.0 client identifier"""

    client_secret: str
    """OAuth 2.0 client secret (will be encrypted and stored securely)"""

    description: Optional[str]
    """Human-readable description"""

    metadata: object
    """Provider metadata"""

    protocols: Protocols
    """Protocol-specific configuration for provider creation"""


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for provider creation"""

    authorization_endpoint: str

    authorization_parameters: Dict[str, str]
    """Custom query parameters appended to authorization redirect URLs.

    Use for non-standard providers (e.g. Google prompt=consent,
    access_type=offline).
    """

    authorization_resource_enabled: bool
    """Whether to include the resource parameter in authorization requests."""

    authorization_resource_parameter: str
    """The resource parameter value to include in authorization requests.

    Defaults to "resource" when authorization_resource_enabled is true.
    """

    code_challenge_methods_supported: SequenceNotStr[str]

    issuer: str
    """OIDC issuer URL for discovery and token validation.

    When omitted, the provider identifier is used as the issuer. New clients should
    always set this explicitly.
    """

    jwks_uri: str

    registration_endpoint: str

    scope_parameter: str
    """The query parameter name for scopes in authorization requests.

    Defaults to "scope". Slack v2 uses "user_scope".
    """

    scope_separator: str
    """The separator character for scope values.

    Defaults to " " (space). Slack v2 uses ",".
    """

    scopes_supported: SequenceNotStr[str]

    token_endpoint: str

    token_response_access_token_pointer: str
    """Dot-separated path to the access token in the token response body.

    Defaults to "access_token". Slack v2 uses "authed_user.access_token".
    """


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration for provider creation"""

    user_identifier_claim: str
    """
    Name of a top-level string claim in this provider's ID Token to use as the user
    identifier on user creation. When not set, the user's Keycard ID is used.
    """

    userinfo_endpoint: str


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration for provider creation"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for provider creation"""

    openid: ProtocolsOpenid
    """OpenID Connect protocol configuration for provider creation"""
