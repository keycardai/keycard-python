# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .package import Package
from ..._models import BaseModel

__all__ = ["PackageList", "Pagination"]


class Pagination(BaseModel):
    """Cursor-based pagination metadata returned alongside a list of results"""

    after_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    before_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    total_count: Optional[int] = None
    """Total number of items across all pages.

    Only present when the request includes ?expand[]=total_count.
    """


class PackageList(BaseModel):
    items: List[Package]

    pagination: Pagination
    """Cursor-based pagination metadata returned alongside a list of results"""
