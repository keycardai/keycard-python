# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ApplicationCredentialListParams"]


class ApplicationCredentialListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    application_id: Annotated[str, PropertyInfo(alias="applicationId")]

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[Union[Literal["total_count"], List[Literal["total_count"]]], PropertyInfo(alias="expand[]")]

    filter_owner_type_ne: Annotated[Literal["platform", "customer"], PropertyInfo(alias="filter[owner_type][ne]")]
    """Exclude credentials whose owning application has this owner type, e.g.

    `filter[owner_type][ne]=platform` returns only credentials of org-created
    applications.
    """

    filter_traits_ne: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[traits][ne]")]
    """Exclude credentials whose owning application has this trait.

    A single value excludes that trait; repeated params accumulate into a not-in set
    (max 100), so a credential matches when its application's traits contain none of
    them. Each value is a single literal trait; a comma is a literal character in
    the value, not a delimiter.
    """

    filter_type: Annotated[
        Union[
            Literal["token", "password", "public-key", "url", "public"],
            List[Literal["token", "password", "public-key", "url", "public"]],
        ],
        PropertyInfo(alias="filter[type]"),
    ]
    """Filter by credential type; repeated values are OR'd, e.g.

    `filter[type]=token&filter[type]=password`.
    """

    limit: int
    """Maximum number of items to return"""

    query: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[]")]
    """
    Search across credential identifier and linked provider name (substring match,
    OR'd across repeated values)
    """

    query_identifier: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[identifier]")]
    """Search by credential identifier (substring match, OR'd across repeated values)"""

    query_provider_name: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="query[provider_name]")]
    """
    Search by the linked provider's name (substring match, OR'd across repeated
    values)
    """

    slug: str

    sort: str
    """Comma-separated sort fields. Prefix with - for descending. Allowed: created_at"""
