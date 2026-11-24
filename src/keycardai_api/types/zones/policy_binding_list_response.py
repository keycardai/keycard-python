# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .policy_set_binding import PolicySetBinding

__all__ = ["PolicyBindingListResponse"]


class PolicyBindingListResponse(BaseModel):
    items: List[PolicySetBinding]
