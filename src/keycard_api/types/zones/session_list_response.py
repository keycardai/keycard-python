# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .session import Session
from ..._models import BaseModel

__all__ = ["SessionListResponse"]


class SessionListResponse(BaseModel):
    items: List[Session]
