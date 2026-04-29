# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionListPoliciesParams"]


class VersionListPoliciesParams(TypedDict, total=False):
    zone_id: Required[str]

    policy_set_id: Required[str]

    after: str
    """Cursor for forward pagination.

    Returned in `Pagination.after_cursor`. Mutually exclusive with `before`.
    """

    before: str
    """Cursor for backward pagination.

    Returned in `Pagination.before_cursor`. Mutually exclusive with `after`.
    """

    expand: List[Literal["total_count"]]
    """**Deprecated.** Use `expand[]` instead.

    Opt-in to additional response fields. Still honored for backward compatibility;
    supplying both `expand` and `expand[]` with disagreeing values returns
    `400 Bad Request`.
    """

    format: Literal["cedar", "json"]
    """Narrows which Cedar representation the response includes.

    When omitted, both `cedar_json` and `cedar_raw` are populated. Pass `json` to
    receive only `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that
    don't care about payload size can skip this parameter.
    """

    limit: int
    """Maximum number of items to return per page."""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
