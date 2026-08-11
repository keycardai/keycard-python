# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .application_trait import ApplicationTrait

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    filter_id: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[id]")]
    """Restrict results to applications with this publicId.

    Repeatable, max 100. Mutually exclusive with after/before.
    """

    filter_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[identifier]")]
    """Filter by exact application identifier"""

    filter_slug: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[slug]")]
    """Filter by exact application slug"""

    identifier: str

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """Search across name and identifier (substring match)"""

    query_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[identifier]")]
    """Search by identifier (substring match)"""

    query_name: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[name]")]
    """Search by name (substring match)"""

    slug: str

    sort: str
    """Comma-separated sort fields.

    Prefix with - for descending. Allowed: created_at, name, identifier
    """

    traits: List[ApplicationTrait]
    """
    Filter by traits (OR matching - returns applications with any of the specified
    traits)
    """

    traits_all: Annotated[List[ApplicationTrait], PropertyInfo(alias="traits[all]")]
    """
    Filter by traits (AND matching - returns applications with all of the specified
    traits)
    """
