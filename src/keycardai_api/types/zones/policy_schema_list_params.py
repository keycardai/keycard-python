# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySchemaListParams"]


class PolicySchemaListParams(TypedDict, total=False):
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

    filter_default: Annotated[bool, PropertyInfo(alias="filter[default]")]
    """Filter schemas by default status.

    When `true`, returns only the zone's default schema. When `false`, returns only
    non-default schemas. Omit to return all schemas.
    """

    format: Literal["cedar", "json"]
    """Schema representation format.

    `cedar` returns human-readable Cedar syntax in `cedar_schema`, `json` returns
    Cedar JSON schema object in `cedar_schema_json`.
    """

    is_default: bool
    """**Deprecated.** Use `filter[default]` instead.

    Filter schemas by default status. When `true`, returns only the zone's default
    schema. When `false`, returns only non-default schemas. Omit to return all
    schemas.

    Still honored for backward compatibility. Supplying both `is_default` and
    `filter[default]` with conflicting values returns `400 Bad Request`.
    """

    limit: int
    """Maximum number of items to return per page."""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
