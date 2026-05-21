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

    email_verified: bool
    """Whether the email address has been verified"""

    identifier: str
    """Zone-scoped user identifier.

    Defaults to the user's Keycard ID. When the provider has user_identifier_claim
    configured, the value is set from that claim at user creation time.
    """

    organization_id: str
    """Organization that owns this user"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this user belongs to"""

    authenticated_at: Optional[str] = None
    """Date when the user was last authenticated"""

    grant_count: Optional[int] = None
    """Delegated-grant count for this user.

    Populated only when `expand[]=grant_count` is set on the listing endpoint.
    """

    issuer: Optional[str] = None
    """Issuer identifier of the identity provider"""

    provider_id: Optional[str] = None
    """Reference to the identity provider.

    This field is undefined when the source identity provider is deleted but the
    user is not deleted.
    """

    session_count: Optional[int] = None
    """Session count for this user.

    Populated only when `expand[]=session_count` is set on the listing endpoint.
    """

    subject: Optional[str] = None
    """Subject identifier from the identity provider"""
