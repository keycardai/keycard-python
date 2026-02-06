# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ServiceAccountListResponse", "Item", "PageInfo"]


class Item(BaseModel):
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


class ServiceAccountListResponse(BaseModel):
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
