# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .application import Application
from ..page_info_pagination import PageInfoPagination

__all__ = ["ApplicationListResponse"]


class ApplicationListResponse(BaseModel):
    items: List[Application]

    page_info: PageInfoPagination
    """Pagination information"""
