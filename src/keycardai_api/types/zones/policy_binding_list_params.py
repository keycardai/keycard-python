# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PolicyBindingListParams"]


class PolicyBindingListParams(TypedDict, total=False):
    filter_mode: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[mode]")]
    """Filter on binding `mode`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention.

    Allowed values: `active`, `shadow`. Unknown values return 400 with the list of
    allowed values. Comma-separated single values are rejected with a 400 pointing
    at the repeated-parameter OR form.

    **Defaults to `shadow`** when omitted (and the deprecated bare `mode` parameter
    is absent), preserving the endpoint's historical shadow-only listing. Pass
    `filter[mode]=active` (or both values) to widen.
    """

    filter_target_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[target_id]")]
    """Filter on `target_id`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention.

    Zone-targeted elements carry the zone ID as their `target_id`. When the
    effective `filter[target_type]` set is exactly `zone` (including via its
    default), any `filter[target_id]` value other than the path `zone_id` returns
    `400 Bad Request`.
    """

    filter_target_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[target_type]")]
    """Filter on `target_type`.

    Repeatable; repeated instances OR across values. See `FilterValues` in the
    shared spec for the full wire convention.

    Allowed values: `zone`, `user` (`resource` and `session` are reserved and not
    yet accepted). Unknown values return 400 with the list of allowed values.
    Comma-separated single values are rejected with a 400 pointing at the
    repeated-parameter OR form.

    **Defaults to `zone`** when omitted (and no deprecated equivalent parameter is
    supplied), so listings exclude principal-scoped elements unless explicitly
    widened. On `listPolicies` the default is skipped when `filter[id]` is present,
    so by-ID fetches resolve regardless of target.

    Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
    `items.enum`) so the server can return a targeted error for the comma-AND form
    instead of a generic "not in allowed values" response.
    """

    mode: Literal["shadow"]
    """**Deprecated.** Use `filter[mode]` instead.

    Still honored for backward compatibility but only accepts `shadow`; other values
    return 400. Conflicts with `filter[mode]` return 400.
    """

    scope_type: Literal["zone"]
    """**Deprecated.** Use `filter[target_type]` instead.

    Still honored for backward compatibility but only accepts `zone`; other values
    return 400. Conflicts with `filter[target_type]` return 400.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
