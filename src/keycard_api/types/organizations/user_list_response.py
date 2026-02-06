# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserListResponse", "Item", "PageInfo"]


class Item(BaseModel):
    id: str
    """The keycard account ID"""

    created_at: datetime
    """The time the entity was created in utc"""

    role: Literal["org_admin", "org_member", "org_viewer"]
    """User's role in the organization"""

    source: str
    """Identity provider issuer"""

    status: Literal["active", "disabled"]
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


class PageInfo(BaseModel):
    """Pagination information using cursor-based pagination"""

    has_next_page: bool
    """Whether there are more items after the current page"""

    has_prev_page: bool
    """Whether there are more items before the current page"""

    end_cursor: Optional[str] = None
    """Cursor pointing to the last item in the current page"""

    start_cursor: Optional[str] = None
    """Cursor pointing to the first item in the current page"""


class UserListResponse(BaseModel):
    items: List[Item]

    page_info: PageInfo
    """Pagination information using cursor-based pagination"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
