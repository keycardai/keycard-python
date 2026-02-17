# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .user import User
from ..._models import BaseModel

__all__ = ["UserListResponse", "Pagination"]


class Pagination(BaseModel):
    """Cursor-based pagination metadata"""

    after_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    before_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    total_count: Optional[int] = None
    """Total number of items matching the query.

    Only included when expand[]=total_count is requested.
    """


class UserListResponse(BaseModel):
    items: List[User]

    pagination: Pagination
    """Cursor-based pagination metadata"""
