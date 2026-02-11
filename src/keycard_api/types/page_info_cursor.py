# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageInfoCursor"]


class PageInfoCursor(BaseModel):
    """Pagination information using cursor-based pagination"""

    has_next_page: bool
    """Whether there are more items after the current page"""

    has_prev_page: bool
    """Whether there are more items before the current page"""

    end_cursor: Optional[str] = None
    """Cursor pointing to the last item in the current page"""

    start_cursor: Optional[str] = None
    """Cursor pointing to the first item in the current page"""
