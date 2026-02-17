# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Provider", "Protocols", "ProtocolsOauth2", "ProtocolsOpenid"]


class ProtocolsOauth2(BaseModel):
    """OAuth 2.0 protocol configuration"""

    authorization_endpoint: Optional[str] = None

    authorization_resource_enabled: Optional[bool] = None
    """Whether to include the resource parameter in authorization requests."""

    authorization_resource_parameter: Optional[str] = None
    """The resource parameter value to include in authorization requests.

    Defaults to "resource" when authorization_resource_enabled is true.
    """

    code_challenge_methods_supported: Optional[List[str]] = None

    jwks_uri: Optional[str] = None

    registration_endpoint: Optional[str] = None

    scope_parameter: Optional[str] = None
    """The query parameter name for scopes in authorization requests.

    Defaults to "scope". Slack v2 uses "user_scope".
    """

    scope_separator: Optional[str] = None
    """The separator character for scope values.

    Defaults to " " (space). Slack v2 uses ",".
    """

    scopes_supported: Optional[List[str]] = None

    token_endpoint: Optional[str] = None

    token_response_access_token_pointer: Optional[str] = None
    """Dot-separated path to the access token in the token response body.

    Defaults to "access_token". Slack v2 uses "authed_user.access_token".
    """


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

    metadata: Optional[object] = None
    """Provider metadata"""

    protocols: Optional[Protocols] = None
    """Protocol-specific configuration"""

    type: Optional[Literal["external", "keycard-vault", "keycard-sts"]] = None
