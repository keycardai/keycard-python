# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .application import Application

__all__ = ["BaseFields"]


class BaseFields(BaseModel):
    """Common fields shared by all application credential types"""

    id: str
    """Unique identifier of the credential"""

    application_id: str
    """ID of the application this credential belongs to"""

    created_at: datetime
    """Entity creation timestamp"""

    organization_id: str
    """Organization that owns this credential"""

    slug: str
    """URL-safe identifier, unique within the zone"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this credential belongs to"""

    application: Optional[Application] = None
    """
    An Application is a software system with an associated identity that can access
    Resources. It may act on its own behalf (machine-to-machine) or on behalf of a
    user (delegated access).
    """
