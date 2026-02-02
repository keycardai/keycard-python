# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .zone_member import ZoneMember
from ..page_info_pagination import PageInfoPagination

__all__ = ["MemberListResponse"]


class MemberListResponse(BaseModel):
    items: List[ZoneMember]

    page_info: PageInfoPagination
    """Pagination information"""
