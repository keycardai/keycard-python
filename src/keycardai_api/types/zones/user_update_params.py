# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    identifier: str
    """Zone-scoped user identifier"""

    status: Literal["active", "disabled"]
    """Status of the user.

    Set to `disabled` to prevent the user from authenticating and revoke their
    active sessions, or `active` to re-enable.
    """
