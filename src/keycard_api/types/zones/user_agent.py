# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserAgent"]


class UserAgent(BaseModel):
    """
    A User Agent represents a user agent (browser, desktop app, CLI tool) that can initiate user sessions via OAuth 2.0 Dynamic Client Registration.
    """

    id: str
    """Unique identifier of the user agent"""

    created_at: datetime
    """Entity creation timestamp"""

    identifier: str
    """User agent identifier (serves as OAuth client_id). Format: ua:{sha256_hash}"""

    name: str
    """Human-readable name"""

    organization_id: str
    """Organization that owns this user agent"""

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this user agent belongs to"""
