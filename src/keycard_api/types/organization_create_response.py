# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrganizationCreateResponse"]


class OrganizationCreateResponse(BaseModel):
    id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    created_at: datetime
    """The time the entity was created in utc"""

    label: str
    """A domain name segment for the entity, often derived from the name."""

    name: str
    """A name for the entity to be displayed in UI"""

    sso_enabled: bool
    """Whether SSO is enabled for this organization"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
