# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MetadataUpdateParam"]


class MetadataUpdateParam(TypedDict, total=False):
    """Entity metadata (set to null or {} to remove metadata)"""

    docs_url: Optional[str]
    """Documentation URL (set to null to unset)"""
