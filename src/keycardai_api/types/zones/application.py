# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Application", "Protocols", "ProtocolsOauth2"]


class ProtocolsOauth2(BaseModel):
    """OAuth 2.0 protocol configuration"""

    post_logout_redirect_uris: Optional[List[str]] = None
    """OAuth 2.0 post-logout redirect URIs for this application"""

    redirect_uris: Optional[List[str]] = None
    """OAuth 2.0 redirect URIs for this application"""


class Protocols(BaseModel):
    """Protocol-specific configuration"""

    oauth2: Optional[ProtocolsOauth2] = None
    """OAuth 2.0 protocol configuration"""


class Application(BaseModel):
    """
    An Application is a software system with an associated identity that can access Resources. It may act on its own behalf (machine-to-machine) or on behalf of a user (delegated access).
    """

    id: str
    """Unique identifier of the application"""

    created_at: datetime
    """Entity creation timestamp"""

    dependencies_count: int
    """Number of resource dependencies"""

    identifier: str
    """User specified identifier, unique within the zone"""

    name: str
    """Human-readable name"""

    organization_id: str
    """Organization that owns this application"""

    owner_type: Literal["platform", "customer"]
    """Who owns this application.

    Platform-owned applications cannot be modified via API.
    """

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this application belongs to"""

    description: Optional[str] = None
    """Human-readable description"""

    metadata: Optional[Metadata] = None
    """Entity metadata"""

    protocols: Optional[Protocols] = None
    """Protocol-specific configuration"""
