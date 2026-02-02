# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .resource import Resource
from ...._models import BaseModel
from ...page_info_pagination import PageInfoPagination

__all__ = ["DependencyListResponse"]


class DependencyListResponse(BaseModel):
    items: List[Resource]

    page_info: PageInfoPagination
    """Pagination information"""
