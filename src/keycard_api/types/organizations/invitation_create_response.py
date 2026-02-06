# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InvitationCreateResponse"]


class InvitationCreateResponse(BaseModel):
    id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    created_at: datetime
    """The time the entity was created in utc"""

    created_by: str
    """ID of the user who created the invitation"""

    email: str
    """Email address for the invitation"""

    expires_at: datetime
    """When the invitation expires"""

    organization_id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    role: Literal["org_admin", "org_member", "org_viewer"]
    """Role that will be assigned when invitation is accepted"""

    status: Literal["pending", "accepted", "expired", "revoked"]
    """Status of an invitation"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
