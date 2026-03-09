# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..metadata import Metadata
from ..provider import Provider
from ...._models import BaseModel
from ..application import Application

__all__ = ["Resource"]


class Resource(BaseModel):
    """A Resource is a system that exposes protected information or functionality.

    It requires authentication of the requesting actor, which may be a user or application, before allowing access.
    """

    id: str
    """Unique identifier of the resource"""

    application_type: Literal["native", "web"]
    """The expected type of client for this credential.

    Native clients must use localhost URLs for redirect_uris or URIs with custom
    schemes. Web clients must use https URLs and must not use localhost as the
    hostname.
    """

    created_at: datetime
    """Entity creation timestamp"""

    identifier: str
    """User specified identifier, unique within the zone"""

    name: str
    """Human-readable name"""

    organization_id: str
    """Organization that owns this resource"""

    owner_type: Literal["platform", "customer"]
    """Who owns this resource. Platform-owned resources cannot be modified via API."""

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this resource belongs to"""

    application: Optional[Application] = None
    """
    An Application is a software system with an associated identity that can access
    Resources. It may act on its own behalf (machine-to-machine) or on behalf of a
    user (delegated access).
    """

    application_id: Optional[str] = None
    """ID of the application that provides this resource"""

    credential_provider: Optional[Provider] = None
    """
    A Provider is a system that supplies access to Resources and allows actors
    (Users or Applications) to authenticate.
    """

    credential_provider_id: Optional[str] = None
    """ID of the credential provider for this resource"""

    description: Optional[str] = None
    """Human-readable description"""

    metadata: Optional[Metadata] = None
    """Entity metadata"""

    scopes: Optional[List[str]] = None
    """Scopes supported by the resource"""

    when_accessing: Optional[List[str]] = None
    """List of resource IDs that, when accessed, make this dependency available.

    Only present when this resource is returned as a dependency.
    """
