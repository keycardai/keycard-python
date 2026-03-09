# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from ...page_info_cursor import PageInfoCursor
from .service_account_credential import ServiceAccountCredential

__all__ = ["CredentialListResponse"]


class CredentialListResponse(BaseModel):
    items: List[ServiceAccountCredential]

    page_info: PageInfoCursor
    """Pagination information using cursor-based pagination"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
