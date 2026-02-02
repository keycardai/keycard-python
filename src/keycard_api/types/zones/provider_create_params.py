# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ProviderCreateParams", "Metadata", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


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

    domains: SequenceNotStr[str]
    """Domains for identifier-first login flow.

    Must be globally unique across all providers.
    """

    metadata: Metadata
    """Provider metadata"""

    protocols: Protocols
    """Protocol-specific configuration for provider creation"""


class Metadata(TypedDict, total=False):
    """Provider metadata"""

    internal_claims: Dict[str, object]
    """Additional claims to inject when provider is used for zone login"""


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for provider creation"""

    authorization_endpoint: str

    code_challenge_methods_supported: SequenceNotStr[str]

    jwks_uri: str

    registration_endpoint: str

    scopes_supported: SequenceNotStr[str]

    token_endpoint: str


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration for provider creation"""

    userinfo_endpoint: str


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration for provider creation"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for provider creation"""

    openid: ProtocolsOpenid
    """OpenID Connect protocol configuration for provider creation"""
