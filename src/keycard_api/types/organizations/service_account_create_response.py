# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ServiceAccountCreateResponse"]


class ServiceAccountCreateResponse(BaseModel):
    id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    created_at: datetime
    """The time the entity was created in utc"""

    name: str
    """A name for the entity to be displayed in UI"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    description: Optional[str] = None
    """Optional description of the service account"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
