# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ProviderUpdateParams", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


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

    identifier: str
    """User specified identifier, unique within the zone"""

    metadata: Optional[object]
    """Provider metadata. Set to null to remove all metadata."""

    name: str
    """Human-readable name"""

    protocols: Optional[Protocols]
    """Protocol-specific configuration. Set to null to remove all protocols."""


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration. Set to null to remove all OAuth2 config."""

    authorization_endpoint: Optional[str]

    authorization_resource_enabled: Optional[bool]
    """Whether to include the resource parameter in authorization requests.

    Set to null to unset.
    """

    authorization_resource_parameter: Optional[str]
    """The resource parameter value to include in authorization requests.

    Defaults to "resource" when authorization_resource_enabled is true. Set to null
    to unset.
    """

    code_challenge_methods_supported: Optional[SequenceNotStr[str]]

    issuer: str
    """OIDC issuer URL for discovery and token validation. Cannot be set to null."""

    jwks_uri: Optional[str]

    registration_endpoint: Optional[str]

    scope_parameter: Optional[str]
    """The query parameter name for scopes in authorization requests.

    Defaults to "scope". Set to null to unset.
    """

    scope_separator: Optional[str]
    """The separator character for scope values.

    Defaults to " " (space). Set to null to unset.
    """

    scopes_supported: Optional[SequenceNotStr[str]]

    token_endpoint: Optional[str]

    token_response_access_token_pointer: Optional[str]
    """Dot-separated path to the access token in the token response body.

    Defaults to "access_token". Set to null to unset.
    """


class ProtocolsOpenid(TypedDict, total=False):
    """OpenID Connect protocol configuration. Set to null to remove all OpenID config."""

    userinfo_endpoint: Optional[str]


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration. Set to null to remove all protocols."""

    oauth2: Optional[ProtocolsOauth2]
    """OAuth 2.0 protocol configuration. Set to null to remove all OAuth2 config."""

    openid: Optional[ProtocolsOpenid]
    """OpenID Connect protocol configuration. Set to null to remove all OpenID config."""
