# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySetCreateParams"]


class PolicySetCreateParams(TypedDict, total=False):
    name: Required[str]

    scope_type: Literal["zone"]
    """**Deprecated.** Use `target_type` instead.

    Only `zone` is accepted; use `target_type` for `user` targets.
    """

    target_type: Literal["zone", "user"]
    """What this policy set targets:

    - `"zone"` — applies to all requests in the zone.
    - `"user"` — can be bound to a specific user.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
