# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .organization_role import OrganizationRole
from .organization_status import OrganizationStatus

__all__ = ["OrganizationUser"]


class OrganizationUser(BaseModel):
    id: str
    """The keycard account ID"""

    created_at: datetime
    """The time the entity was created in utc"""

    role: OrganizationRole
    """User's role in the organization"""

    source: str
    """Identity provider issuer"""

    status: OrganizationStatus
    """Status of organization membership"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    email: Optional[str] = None
    """User email address"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
