# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZoneUpdateParams", "EncryptionKey", "Protocols", "ProtocolsOauth2"]


class ZoneUpdateParams(TypedDict, total=False):
    cname: Optional[str]
    """Custom domain name (CNAME) for the zone (set to null to remove)"""

    default_mcp_gateway_application_id: Optional[str]
    """
    Application ID configured as the default MCP Gateway for the zone (set to null
    to unset)
    """

    description: Optional[str]
    """Human-readable description"""

    directory_open_signups_enabled: bool
    """
    Whether directory open signups are enabled for the zone, only applies when
    user_identity_provider_id is not set
    """

    encryption_key: Optional[EncryptionKey]
    """
    AWS KMS configuration for zone encryption update (set to null to remove
    customer-managed key and revert to default)
    """

    login_flow: Optional[Literal["default", "identifier_first"]]
    """Login flow style for the zone.

    'default' uses standard authentication, 'identifier_first' uses identifier-based
    provider routing. Set to null to reset to 'default'.
    """

    name: str
    """Human-readable name"""

    protocols: Optional[Protocols]
    """Protocol configuration update for a zone (partial update)"""

    user_identity_provider_id: Optional[str]
    """Provider ID to configure for user login (set to null to unset)"""


class EncryptionKey(TypedDict, total=False):
    """
    AWS KMS configuration for zone encryption update (set to null to remove customer-managed key and revert to default)
    """

    arn: Required[str]
    """AWS KMS Key ARN for encrypting the zone's data"""

    type: Required[Literal["aws"]]


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration update for a zone (partial update)"""

    dcr_enabled: Optional[bool]
    """Whether Dynamic Client Registration is enabled"""

    pkce_required: Optional[bool]
    """Whether PKCE is required for authorization code flows"""


class Protocols(TypedDict, total=False):
    """Protocol configuration update for a zone (partial update)"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration update for a zone (partial update)"""
