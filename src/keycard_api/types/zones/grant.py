# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .user import User
from .provider import Provider
from ..._models import BaseModel
from .applications.resource import Resource

__all__ = ["Grant"]


class Grant(BaseModel):
    """User authorization for a resource to be accessed on their behalf.

    The grant links the user, resource, and the provider that issued the grant.
    """

    id: str
    """Unique identifier of the delegated grant"""

    created_at: datetime
    """Entity creation timestamp"""

    expires_at: datetime
    """Date when grant expires"""

    organization_id: str
    """Organization that owns this grant"""

    provider_id: str
    """ID of the provider that issued this grant"""

    resource_id: str
    """ID of resource receiving grant"""

    scopes: List[str]
    """Granted OAuth scopes"""

    status: Literal["active", "expired", "revoked"]

    updated_at: datetime
    """Entity update timestamp"""

    user_id: str
    """Reference to the user granting permission"""

    zone_id: str
    """Zone this grant belongs to"""

    active: Optional[bool] = None
    """Whether the grant is currently active (deprecated - use status instead)"""

    provider: Optional[Provider] = None
    """
    A Provider is a system that supplies access to Resources and allows actors
    (Users or Applications) to authenticate.
    """

    resource: Optional[Resource] = None
    """A Resource is a system that exposes protected information or functionality.

    It requires authentication of the requesting actor, which may be a user or
    application, before allowing access.
    """

    user: Optional[User] = None
    """An authenticated user entity"""
