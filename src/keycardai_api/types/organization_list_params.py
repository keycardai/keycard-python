# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: List[Literal["permissions", "total_count"]]
    """Fields to expand in the response.

    Supports "permissions" to include the permissions field with the caller's
    permissions for the resource. For list organization identities only,
    "total_count" populates pagination.total_count with the number of identities
    matching the same filters as the list (excluding cursor and limit). Other
    operations ignore expand values they do not use.
    """

    limit: int
    """Maximum number of organizations to return"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
