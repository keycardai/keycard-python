# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["SecretListResponse", "SecretListResponseItem"]


class SecretListResponseItem(BaseModel):
    id: str
    """A globally unique opaque identifier"""

    created_at: datetime

    entity_id: str
    """A globally unique opaque identifier"""

    name: str
    """A name for the entity to be displayed in UI"""

    type: Literal["token", "password"]

    updated_at: datetime

    version: int

    zone_id: str
    """A globally unique opaque identifier"""

    description: Optional[str] = None
    """A description of the entity"""

    metadata: Optional[object] = None
    """A JSON object containing arbitrary metadata. Metadata will not be encrypted."""


SecretListResponse: TypeAlias = List[SecretListResponseItem]
