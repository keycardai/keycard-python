# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..page_info_pagination import PageInfoPagination
from .applications.resource import Resource

__all__ = ["ApplicationListResourcesResponse"]


class ApplicationListResourcesResponse(BaseModel):
    items: List[Resource]

    page_info: PageInfoPagination
    """Pagination information"""
