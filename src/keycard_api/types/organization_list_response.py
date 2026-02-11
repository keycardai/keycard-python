# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .organization import Organization
from .page_info_cursor import PageInfoCursor

__all__ = ["OrganizationListResponse"]


class OrganizationListResponse(BaseModel):
    items: List[Organization]

    page_info: PageInfoCursor
    """Pagination information using cursor-based pagination"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
