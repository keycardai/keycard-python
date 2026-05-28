# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    zone_id: Required[str]

    after: str
    """Cursor for forward pagination.

    Returned in `Pagination.after_cursor`. Mutually exclusive with `before`.
    """

    before: str
    """Cursor for backward pagination.

    Returned in `Pagination.before_cursor`. Mutually exclusive with `after`.
    """

    limit: int
    """Maximum number of items to return per page."""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
