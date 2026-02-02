# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .credential import Credential
from ..page_info_pagination import PageInfoPagination

__all__ = ["ApplicationListCredentialsResponse"]


class ApplicationListCredentialsResponse(BaseModel):
    items: List[Credential]

    page_info: PageInfoPagination
    """Pagination information"""
