# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    cursor: str

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to providers with this ID. Repeatable, max 100."""

    identifier: str

    limit: int
    """Maximum number of items to return"""

    slug: str

    type: Literal["external", "keycard-vault", "keycard-sts"]
