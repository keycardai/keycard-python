# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySetCloneParams"]


class PolicySetCloneParams(TypedDict, total=False):
    zone_id: Required[str]

    name: Required[str]
    """Name of the new policy set. 409 `policy_set_name_conflict` on collision."""

    copy_policies: Literal["none", "platform", "all"]
    """
    Which pinned policies are duplicated as new customer-owned policies. `none`
    shares every pin; `platform` copies platform-owned pins and shares
    customer-owned ones; `all` copies every pin.
    """

    source_version_id: str
    """Policy set version public ID on the source set.

    Defaults to the source's latest non-archived version.
    """

    target_type: Literal["zone", "user"]
    """Defaults to the source set's target type."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
