# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID or label identifier"""

    role: Literal["org_admin", "org_member", "org_viewer"]
    """New role for the user in the organization"""

    status: Literal["active", "disabled"]
    """New status for the user in the organization"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
