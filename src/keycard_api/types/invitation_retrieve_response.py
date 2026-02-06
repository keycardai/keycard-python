# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

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

    role: Literal["org_admin", "org_member", "org_viewer"]
    """Role that will be assigned when invitation is accepted"""

    status: Literal["pending", "accepted", "expired", "revoked"]
    """Status of an invitation"""
