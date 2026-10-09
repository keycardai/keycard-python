# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ServiceAccountListParams"]


class ServiceAccountListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: Annotated[
        Union[Literal["permissions", "total_count"], List[Literal["permissions", "total_count"]]],
        PropertyInfo(alias="expand[]"),
    ]
    """Fields to expand in the response.

    Supports "permissions" to include the permissions field with the caller's
    permissions for the resource. For the service account and service account
    credential list operations, "total_count" populates pagination.total_count with
    the number of items matching the same filters as the list (excluding cursor and
    limit). Other operations ignore expand values they do not use.
    """

    limit: int
    """Maximum number of service accounts to return"""

    query: SequenceNotStr[str]
    """
    Search service accounts by name or description (case-insensitive substring
    match). When multiple values are provided, a service account matches if it
    matches any of them.
    """

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
