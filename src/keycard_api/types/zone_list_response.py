# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .zone import Zone
from .._models import BaseModel
from .page_info_pagination import PageInfoPagination

__all__ = ["ZoneListResponse", "Pagination"]


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


class ZoneListResponse(BaseModel):
    items: List[Zone]

    page_info: PageInfoPagination
    """Pagination information"""

    pagination: Pagination
    """Cursor-based pagination metadata"""
