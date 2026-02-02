# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .zone import Zone
from .._models import BaseModel
from .page_info_pagination import PageInfoPagination

__all__ = ["ZoneListResponse"]


class ZoneListResponse(BaseModel):
    items: List[Zone]

    page_info: PageInfoPagination
    """Pagination information"""
