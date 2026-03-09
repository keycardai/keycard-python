# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .organization_role import OrganizationRole
from .organization_status import OrganizationStatus

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID or label identifier"""

    role: OrganizationRole
    """New role for the user in the organization"""

    status: OrganizationStatus
    """New status for the user in the organization"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
