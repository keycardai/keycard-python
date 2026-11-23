# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .invitation_status import InvitationStatus
from .organization_role import OrganizationRole

__all__ = ["Invitation"]


class Invitation(BaseModel):
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

    role: OrganizationRole
    """Role that will be assigned when invitation is accepted"""

    status: InvitationStatus
    """Status of an invitation"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    delivery_status: Optional[Literal["queued", "sending", "sent", "failed", "expired"]] = None
    """Delivery state of the most recent invitation email.

    `queued` and `sending` mean the email service still holds the message. `sent`
    means the provider accepted it. `failed` means the email service could not be
    reached or rejected the message. `expired` means the invitation expired before
    the message was delivered. Absent for invitations created before delivery
    tracking existed.
    """

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
