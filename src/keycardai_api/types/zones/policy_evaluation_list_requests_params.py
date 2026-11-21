# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PolicyEvaluationListRequestsParams"]


class PolicyEvaluationListRequestsParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination.

    Returned in `Pagination.after_cursor`. Mutually exclusive with `before`.
    """

    before: str
    """Cursor for backward pagination.

    Returned in `Pagination.before_cursor`. Mutually exclusive with `after`.
    """

    expand: Annotated[
        Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]], PropertyInfo(alias="expand[]")
    ]
    """Opt-in to additional response fields (`total_count`, `user`).

    Repeatable; matches the `expand[]` convention used across the Keycard API.
    """

    filter_active_decision: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[active_decision]")]
    """Filter on `active_decision`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention.

    Allowed values: `allow`, `deny`. Unknown values return 400 with the list of
    allowed values. Comma-separated single values are rejected with a 400 pointing
    at the repeated-parameter OR form.

    Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
    `items.enum`) so the server can return a targeted error for the comma-AND form
    instead of a generic "not in allowed values" response.
    """

    filter_authority_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[authority_type]")]
    """Filter on `authority_type`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention. Rows with `NULL` authority_type are
    excluded when this filter is present.

    Allowed values: `delegation`, `impersonation`. Unknown values return 400 with
    the list of allowed values. Comma-separated single values are rejected with a
    400 pointing at the repeated-parameter OR form.

    Note: the allowed-value enum is enforced in the handler.
    """

    filter_has_shadow: Annotated[bool, PropertyInfo(alias="filter[has_shadow]")]
    """Filter by shadow-evaluation presence.

    When `true`, returns only requests that had a shadow policy set version
    (`shadow_psv_id IS NOT NULL`). When `false`, returns only requests without one.
    Omit to return all.
    """

    filter_principal_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[principal_id]")]
    """Filter on `principal_id` by exact match.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention. Comma-separated single values are
    rejected with a 400 pointing at the repeated-parameter OR form.
    """

    filter_principal_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[principal_type]")]
    """Filter on `principal_type`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention.

    Allowed values: `user`, `application`. Unknown values return 400 with the list
    of allowed values. Comma-separated single values are rejected with a 400
    pointing at the repeated-parameter OR form.

    Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
    `items.enum`) so the server can return a targeted error for the comma-AND form.
    """

    filter_resource_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[resource_id]")]
    """Filter on `resource_id` by exact match.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention. Comma-separated single values are
    rejected with a 400 pointing at the repeated-parameter OR form.
    """

    filter_subject_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[subject_id]")]
    """Filter on `subject_id` by exact match.

    Repeatable; repeated instances OR across values. Rows with `NULL` subject_id are
    excluded when this filter is present. See `FilterValues` in the shared spec for
    the full wire convention.
    """

    filter_subject_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[subject_type]")]
    """Filter on `subject_type`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention. Rows with `NULL` subject_type are
    excluded when this filter is present.

    Allowed values: `user`, `application`. Unknown values return 400 with the list
    of allowed values. Comma-separated single values are rejected with a 400
    pointing at the repeated-parameter OR form.

    Note: the allowed-value enum is enforced in the handler.
    """

    limit: int
    """Maximum number of items to return per page."""

    order: Literal["asc", "desc"]
    """Sort direction. Default is desc (newest first)."""

    query_action: Annotated[SequenceNotStr[str], PropertyInfo(alias="query[action]")]
    """Case-insensitive substring search on `action`.

    Repeatable; if multiple terms are supplied they are OR-ed.
    """

    sort: Literal["created_at"]
    """Field to sort by."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
