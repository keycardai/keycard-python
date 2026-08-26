# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..user import User
from ...._models import BaseModel

__all__ = ["GroupMember"]


class GroupMember(BaseModel):
    """A user's membership in a group"""

    created_at: datetime
    """Entity creation timestamp"""

    user_id: str
    """ID of the user"""

    user: Optional[User] = None
    """An authenticated user entity"""
