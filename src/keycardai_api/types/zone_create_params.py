# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .encryption_key_aws_kms_config_param import EncryptionKeyAwsKmsConfigParam

__all__ = ["ZoneCreateParams", "Protocols", "ProtocolsOauth2"]


class ZoneCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    default_mcp_gateway_application: bool
    """Assign a default MCP Gateway application to the zone"""

    description: Optional[str]
    """Human-readable description.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    encryption_key: EncryptionKeyAwsKmsConfigParam
    """AWS KMS configuration for zone encryption.

    When not specified, the default Keycard Cloud encryption key will be used.
    """

    login_flow: Literal["default", "identifier_first"]
    """Login flow style for the zone.

    'default' uses standard authentication, 'identifier_first' uses identifier-based
    provider routing.
    """

    protocols: Protocols
    """Protocol configuration for zone creation"""

    requires_invitation: bool
    """
    Whether the zone requires an invitation for email/password registration, only
    applies when user_identity_provider_id is not set. Defaults to true.
    """


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for zone creation"""

    dcr_enabled: bool
    """Whether Dynamic Client Registration is enabled"""

    pkce_required: bool
    """Whether PKCE is required for authorization code flows"""


class Protocols(TypedDict, total=False):
    """Protocol configuration for zone creation"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for zone creation"""
