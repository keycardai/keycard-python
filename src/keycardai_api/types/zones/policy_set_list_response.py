# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .policy_set_with_binding import PolicySetWithBinding

__all__ = ["PolicySetListResponse", "Pagination"]


class Pagination(BaseModel):
    after_cursor: Optional[str] = None
    """Cursor of the last item on the current page.

    Pass to after for the next page. Null when there is no next page.
    """

    before_cursor: Optional[str] = None
    """Cursor of the first item on the current page.

    Pass to before for the previous page. Null when there is no previous page.
    """

    total_count: Optional[int] = None
    """Total number of items matching the current filters.

    Only included when expand=total_count is requested.
    """


class PolicySetListResponse(BaseModel):
    items: List[PolicySetWithBinding]

    pagination: Pagination
