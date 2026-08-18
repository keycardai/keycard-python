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

    filter_owner_type: Annotated[Literal["platform", "customer"], PropertyInfo(alias="filter[owner_type]")]
    """Filter by owner type: `platform` (Keycard-managed) or `customer` (org-created)."""

    filter_traits: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="filter[traits]")]
    """Filter by trait.

    Comma-separated values (`a,b`) are AND'd; repeated params are OR'd.
    """

    identifier: str
    """
    Backward-compatible alias for `filter[identifier]`: exact match on a single
    resource identifier.
    """

    limit: int
    """Maximum number of items to return"""

    slug: str
