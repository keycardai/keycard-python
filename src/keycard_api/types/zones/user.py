# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    """An authenticated user entity"""

    id: str
    """Unique identifier of the user"""

    created_at: datetime
    """Entity creation timestamp"""

    email: str
    """Email address of the user"""

    issuer: str
    """Issuer identifier of the identity provider"""

    organization_id: str
    """Organization that owns this user"""

    subject: str
    """Subject identifier from the identity provider"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this user belongs to"""

    authenticated_at: Optional[str] = None
    """Date when the user was last authenticated"""

    provider_id: Optional[str] = None
    """Reference to the identity provider.

    This field is undefined when the source identity provider is deleted but the
    user is not deleted.
    """
