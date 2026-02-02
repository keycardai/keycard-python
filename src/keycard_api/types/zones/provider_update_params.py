# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ProviderUpdateParams", "Metadata", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class ProviderUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    client_id: Optional[str]
    """OAuth 2.0 client identifier. Set to null to remove."""

    client_secret: Optional[str]
    """OAuth 2.0 client secret (will be encrypted and stored securely).

    Set to null to remove.
    """

    description: Optional[str]
    """Human-readable description"""

    domains: Optional[SequenceNotStr[str]]
    """Domains for identifier-first login flow.

    Must be globally unique across all providers. Set to null to remove all domains.
    """

    identifier: str
    """User specified identifier, unique within the zone"""

    metadata: Optional[Metadata]
    """Provider metadata. Set to null to remove all metadata."""

    name: str
    """Human-readable name"""

    protocols: Optional[Protocols]
    """Protocol-specific configuration. Set to null to remove all protocols."""


class Metadata(TypedDict, total=False):
    """Provider metadata. Set to null to remove all metadata."""

    internal_claims: Optional[Dict[str, object]]
    """Additional claims to inject when provider is used for zone login.

    Set to null to remove.
    """


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration. Set to null to remove all OAuth2 config."""

    authorization_endpoint: Optional[str]

    code_challenge_methods_supported: Optional[SequenceNotStr[str]]

    jwks_uri: Optional[str]

    registration_endpoint: Optional[str]

    scopes_supported: Optional[SequenceNotStr[str]]

    token_endpoint: Optional[str]


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration. Set to null to remove all OpenID config."""

    userinfo_endpoint: Optional[str]


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration. Set to null to remove all protocols."""

    oauth2: Optional[ProtocolsOauth2]
    """OAuth 2.0 protocol configuration. Set to null to remove all OAuth2 config."""

    openid: Optional[ProtocolsOpenid]
    """OpenID Connect protocol configuration. Set to null to remove all OpenID config."""
