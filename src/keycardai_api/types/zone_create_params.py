# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .encryption_key_aws_kms_config_param import EncryptionKeyAwsKmsConfigParam

__all__ = ["ZoneCreateParams", "Protocols", "ProtocolsOauth2", "ProtocolsOauth2Cimd"]


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

    organization_id: str
    """Target organization ID.

    Required for platform principals (whose tokens carry no organization claim); for
    organization-scoped principals it is optional and must match the authenticated
    organization if supplied.
    """

    protocols: Protocols
    """Protocol configuration for zone creation"""

    requires_invitation: bool
    """
    Whether the zone requires an invitation for email/password registration, only
    applies when user_identity_provider_id is not set. Defaults to true.
    """


class ProtocolsOauth2Cimd(TypedDict, total=False):
    """Client ID Metadata Document auto-provisioning configuration"""

    allowed_client_ids: Required[SequenceNotStr[str]]
    """Allowlist for CIMD client_id URLs.

    Each entry is an exact URL, a wildcard origin with a single _ replacing one
    subdomain label (e.g. https://_.example.com matches https://app.example.com but
    not https://a.b.example.com), or the literal _ to allow any client. Only one _
    is permitted per entry.
    """

    enabled: Required[bool]
    """Whether CIMD auto-provisioning is enabled for unregistered URL-based clients"""


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for zone creation"""

    cimd: ProtocolsOauth2Cimd
    """Client ID Metadata Document auto-provisioning configuration"""

    dcr_enabled: bool
    """Whether Dynamic Client Registration is enabled"""

    pkce_required: bool
    """Whether PKCE is required for authorization code flows"""


class Protocols(TypedDict, total=False):
    """Protocol configuration for zone creation"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for zone creation"""
