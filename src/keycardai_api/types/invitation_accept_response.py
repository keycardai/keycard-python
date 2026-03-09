# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InvitationAcceptResponse"]


class InvitationAcceptResponse(BaseModel):
    """Result of accepting an invitation"""

    organization_id: str
    """ID of the organization joined"""

    organization_name: str
    """Name of the organization joined"""

    success: bool
    """Whether the invitation was successfully accepted"""

    user_id: Optional[str] = None
    """ID of the user who accepted the invitation"""
