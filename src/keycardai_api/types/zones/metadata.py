# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    """Entity metadata"""

    docs_url: Optional[str] = None
    """Documentation URL"""
