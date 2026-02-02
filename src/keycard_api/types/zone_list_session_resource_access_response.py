# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["ZoneListSessionResourceAccessResponse", "Item"]


class Item(BaseModel):
    """Aggregated record of session-resource access events"""

    first_accessed_at: datetime
    """When access first occurred"""

    last_accessed_at: datetime
    """When access most recently occurred"""

    organization_id: str
    """Organization ID"""

    resource_id: str
    """Resource ID"""

    session_id: str
    """Session ID"""

    total_access_count: int
    """Total number of access events for this session-resource pair"""


class ZoneListSessionResourceAccessResponse(BaseModel):
    items: List[Item]
