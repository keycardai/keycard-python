# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Provider", "Metadata", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class Metadata(BaseModel):
    """Provider metadata"""

    internal_claims: Optional[Dict[str, object]] = None
    """Additional claims to inject when provider is used for zone login"""


class ProtocolsOauth2(BaseModel):
    """OAuth 2.0 protocol configuration"""

    authorization_endpoint: Optional[str] = None

    code_challenge_methods_supported: Optional[List[str]] = None

    jwks_uri: Optional[str] = None

    registration_endpoint: Optional[str] = None

    scopes_supported: Optional[List[str]] = None

    token_endpoint: Optional[str] = None


class ProtocolsOpenid(BaseModel):
    """OpenID Connect protocol configuration"""

    userinfo_endpoint: Optional[str] = None


class Protocols(BaseModel):
    """Protocol-specific configuration"""

    oauth2: Optional[ProtocolsOauth2] = None
    """OAuth 2.0 protocol configuration"""

    openid: Optional[ProtocolsOpenid] = None
    """OpenID Connect protocol configuration"""


class Provider(BaseModel):
    """
    A Provider is a system that supplies access to Resources and allows actors (Users or Applications) to authenticate.
    """

    id: str
    """Unique identifier of the provider"""

    created_at: datetime
    """Entity creation timestamp"""

    identifier: str
    """User specified identifier, unique within the zone"""

    name: str
    """Human-readable name"""

    organization_id: str
    """Organization that owns this provider"""

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this provider belongs to"""

    client_id: Optional[str] = None
    """OAuth 2.0 client identifier"""

    client_secret_set: Optional[bool] = None
    """Indicates whether a client secret is configured"""

    description: Optional[str] = None
    """Human-readable description"""

    domains: Optional[List[str]] = None
    """Domains for identifier-first login flow.

    Must be globally unique across all providers.
    """

    metadata: Optional[Metadata] = None
    """Provider metadata"""

    protocols: Optional[Protocols] = None
    """Protocol-specific configuration"""

    type: Optional[Literal["external", "keycard-vault", "keycard-sts"]] = None
