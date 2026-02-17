# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .credential import Credential
from ..page_info_pagination import PageInfoPagination

__all__ = ["ApplicationListCredentialsResponse", "Pagination"]


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


class ApplicationListCredentialsResponse(BaseModel):
    items: List[Credential]

    page_info: PageInfoPagination
    """Pagination information"""

    pagination: Pagination
    """Cursor-based pagination metadata"""
