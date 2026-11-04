# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .organizations.invitation_status import InvitationStatus
from .organizations.organization_role import OrganizationRole

__all__ = ["InvitationRetrieveResponse"]


class InvitationRetrieveResponse(BaseModel):
    """Public invitation details viewable by token"""

    created_by_name: str
    """Name of the user who sent the invitation"""

    email: str
    """Email address for the invitation"""

    expires_at: datetime
    """When the invitation expires"""

    organization_name: str
    """Name of the organization being invited to"""

    role: OrganizationRole
    """Role that will be assigned when invitation is accepted"""

    status: InvitationStatus
    """Status of an invitation"""
