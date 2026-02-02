# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .applications.resource import Resource

__all__ = ["ResourceListResponse"]


class ResourceListResponse(BaseModel):
    items: List[Resource]
