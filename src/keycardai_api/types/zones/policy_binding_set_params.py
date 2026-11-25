# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicyBindingSetParams"]


class PolicyBindingSetParams(TypedDict, total=False):
    mode: Required[Literal["shadow"]]
    """Binding mode"""

    policy_set_id: Required[str]
    """Public ID of the policy set to bind"""

    policy_set_version_id: Required[str]
    """Public ID of the policy set version to bind"""

    scope_target_id: str
    """**Deprecated.** Use `target_id` instead."""

    scope_type: Literal["zone"]
    """**Deprecated.** Use `target_type` instead."""

    target_id: str
    """Defaults to zone_id for zone targets. Required for other targets."""

    target_type: Literal["zone"]
    """What the binding targets. Only `zone` is supported for direct binding writes."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
