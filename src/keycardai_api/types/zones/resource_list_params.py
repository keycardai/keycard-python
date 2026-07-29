# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ResourceListParams"]


class ResourceListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    credential_provider_id: Annotated[str, PropertyInfo(alias="credentialProviderId")]
    """Filter resources by credential provider ID"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    filter_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[identifier]")]
    """Filter by exact resource identifier"""

    identifier: str
    """Filter resources by identifier"""

    limit: int
    """Maximum number of items to return"""

    slug: str

    traits: List[Literal["external", "proxy", "mcp-server"]]
    """
    Filter by traits (OR matching - returns resources with any of the specified
    traits)
    """

    traits_all: Annotated[List[Literal["external", "proxy", "mcp-server"]], PropertyInfo(alias="traits[all]")]
    """
    Filter by traits (AND matching - returns resources with all of the specified
    traits)
    """
