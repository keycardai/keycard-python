# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .grant import Grant
from ..._models import BaseModel

__all__ = ["DelegatedGrantListResponse"]


class DelegatedGrantListResponse(BaseModel):
    items: List[Grant]
