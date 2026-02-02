# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_agent import UserAgent

__all__ = ["UserAgentListResponse"]


class UserAgentListResponse(BaseModel):
    items: List[UserAgent]
