# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .provider import Provider
from ..._models import BaseModel
from ..page_info_pagination import PageInfoPagination

__all__ = ["ProviderListResponse"]


class ProviderListResponse(BaseModel):
    items: List[Provider]

    page_info: PageInfoPagination
    """Pagination information"""
