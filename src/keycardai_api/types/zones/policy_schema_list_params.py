# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySchemaListParams"]


class PolicySchemaListParams(TypedDict, total=False):
    after: str
    """Return items after this cursor (forward pagination).

    Use after_cursor from a previous response. Mutually exclusive with before.
    """

    before: str
    """Return items before this cursor (backward pagination).

    Use before_cursor from a previous response. Mutually exclusive with after.
    """

    expand: List[Literal["total_count"]]
    """Opt-in to additional response fields"""

    format: Literal["cedar", "json"]
    """Schema representation format.

    `cedar` returns human-readable Cedar syntax in `cedar_schema`, `json` returns
    Cedar JSON schema object in `cedar_schema_json`.
    """

    is_default: bool
    """Filter schemas by default status.

    When `true`, returns only the zone's default schema. When `false`, returns only
    non-default schemas. Omit to return all schemas.
    """

    limit: int
    """Maximum number of items to return"""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
