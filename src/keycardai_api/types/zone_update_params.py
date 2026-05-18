# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ZoneUpdateParams", "EncryptionKey", "Protocols", "ProtocolsOauth2", "ProtocolsOauth2Cimd"]


class ZoneUpdateParams(TypedDict, total=False):
    default_mcp_gateway_application_id: Optional[str]
    """
    Application ID configured as the default MCP Gateway for the zone (set to null
    to unset)
    """

    default_resource_id: Optional[str]
    """
    Resource ID to configure as the default resource for the zone (set to null to
    unset)
    """

    description: Optional[str]
    """Human-readable description.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    encryption_key: Optional[EncryptionKey]
    """
    AWS KMS configuration for zone encryption update (set to null to remove
    customer-managed key and revert to default)
    """

    name: str
    """Human-readable name.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    protocols: Optional[Protocols]
    """Protocol configuration update for a zone (partial update)"""

    requires_invitation: bool
    """
    Whether the zone requires an invitation for email/password registration, only
    applies when user_identity_provider_id is not set
    """

    user_identity_provider_id: Optional[str]
    """Provider ID to configure for user login (set to null to unset)"""


class EncryptionKey(TypedDict, total=False):
    """
    AWS KMS configuration for zone encryption update (set to null to remove customer-managed key and revert to default)
    """

    arn: Required[str]
    """AWS KMS Key ARN for encrypting the zone's data"""

    type: Required[Literal["aws"]]


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
    """OAuth 2.0 protocol configuration update for a zone (partial update)"""

    cimd: ProtocolsOauth2Cimd
    """Client ID Metadata Document auto-provisioning configuration"""

    dcr_enabled: Optional[bool]
    """Whether Dynamic Client Registration is enabled"""

    pkce_required: Optional[bool]
    """Whether PKCE is required for authorization code flows"""


class Protocols(TypedDict, total=False):
    """Protocol configuration update for a zone (partial update)"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration update for a zone (partial update)"""
