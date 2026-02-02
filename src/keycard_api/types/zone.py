# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .encryption_key_aws_kms_config import EncryptionKeyAwsKmsConfig

__all__ = ["Zone", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class ProtocolsOauth2(BaseModel):
    """OAuth 2.0 protocol configuration for a zone"""

    authorization_endpoint: str
    """OAuth 2.0 authorization endpoint"""

    authorization_server_metadata: str
    """
    OAuth 2.0 Authorization Server Metadata endpoint
    (.well-known/oauth-authorization-server)
    """

    dcr_enabled: bool
    """Whether Dynamic Client Registration is enabled"""

    issuer: str
    """OAuth 2.0 issuer identifier"""

    jwks_uri: str
    """JSON Web Key Set endpoint"""

    pkce_required: bool
    """Whether PKCE is required for authorization code flows"""

    redirect_uri: str
    """OAuth 2.0 redirect URI for this zone"""

    registration_endpoint: str
    """OAuth 2.0 Dynamic Client Registration endpoint"""

    token_endpoint: str
    """OAuth 2.0 token endpoint"""


class ProtocolsOpenid(BaseModel):
    """OpenID Connect protocol configuration for a zone"""

    provider_configuration: str
    """
    OpenID Connect Provider Configuration endpoint
    (.well-known/openid-configuration)
    """

    userinfo_endpoint: str
    """OpenID Connect UserInfo endpoint"""


class Protocols(BaseModel):
    """Protocol configuration for a zone"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for a zone"""

    openid: ProtocolsOpenid
    """OpenID Connect protocol configuration for a zone"""


class Zone(BaseModel):
    """A zone for organizing resources within an organization"""

    id: str
    """Unique identifier of the zone"""

    created_at: datetime
    """Entity creation timestamp"""

    name: str
    """Human-readable name"""

    organization_id: str
    """Organization that owns this zone"""

    protocols: Protocols
    """Protocol configuration for a zone"""

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    cname: Optional[str] = None
    """Custom domain name (CNAME) for the zone"""

    default_mcp_gateway_application_id: Optional[str] = None
    """Application ID configured as the default MCP Gateway for the zone"""

    description: Optional[str] = None
    """Human-readable description"""

    directory_open_signups_enabled: Optional[bool] = None
    """
    Whether directory open signups are enabled for the zone, only applies when
    user_identity_provider_id is not set
    """

    encryption_key: Optional[EncryptionKeyAwsKmsConfig] = None
    """AWS KMS configuration for zone encryption.

    When not specified, the default Keycard Cloud encryption key will be used.
    """

    login_flow: Optional[Literal["default", "identifier_first"]] = None
    """Login flow style for the zone.

    'default' uses standard authentication, 'identifier_first' uses identifier-based
    provider routing.
    """

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """Permissions granted to the authenticated principal.

    Only populated when expand[]=permissions query parameter is provided. Keys are
    resource types, values are objects mapping action names to boolean values.
    """

    user_identity_provider_id: Optional[str] = None
    """Provider ID configured for user login"""
