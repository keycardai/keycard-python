# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
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

    filter_owner_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[owner_type]")]
    """Filter on `owner_type`.

    Repeatable; repeated instances OR across values (e.g.
    `?filter[owner_type]=platform&filter[owner_type]=customer` matches either). See
    `FilterValues` in the shared spec for the full wire convention.

    Allowed values: `platform`, `customer`. Unknown values return 400 with the list
    of allowed values. Comma-separated single values (e.g.
    `?filter[owner_type]=platform,customer`) are rejected with a 400 pointing at the
    repeated-parameter OR form.

    Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
    `items.enum`) so the server can return a targeted error for the comma-AND form
    instead of a generic "not in allowed values" response.
    """

    limit: int
    """Maximum number of items to return per page."""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    query: SequenceNotStr[str]
    """Case-insensitive substring search across all searchable fields of the resource.

    For policies that is `name` and `description`; for policy sets that is `name`.
    Repeatable; if multiple terms are supplied they are OR-ed.
    """

    query_description: Annotated[SequenceNotStr[str], PropertyInfo(alias="query[description]")]
    """Case-insensitive substring search on `description` (policies only).

    Repeatable; if multiple terms are supplied they are OR-ed.
    """

    query_name: Annotated[SequenceNotStr[str], PropertyInfo(alias="query[name]")]
    """Case-insensitive substring search on `name`.

    Repeatable; if multiple terms are supplied they are OR-ed (any matching term
    returns the row).
    """

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
