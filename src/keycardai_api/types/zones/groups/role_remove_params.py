# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RoleRemoveParams"]


class RoleRemoveParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    group_id: Required[Annotated[str, PropertyInfo(alias="groupId")]]

    scope_id: str
    """Scope target of the grant to revoke. Provide together with scope_type."""

    scope_type: str
    """Scope kind of the grant to revoke. Provide together with scope_id."""
