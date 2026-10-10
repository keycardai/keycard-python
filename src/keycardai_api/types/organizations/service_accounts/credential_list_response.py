# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from ...page_info_cursor import PageInfoCursor
from .service_account_credential import ServiceAccountCredential

__all__ = ["CredentialListResponse", "Pagination"]


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


class CredentialListResponse(BaseModel):
    items: List[ServiceAccountCredential]

    page_info: PageInfoCursor
    """Pagination information using cursor-based pagination"""

    pagination: Pagination
    """Cursor-based pagination metadata returned alongside a list of results"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
