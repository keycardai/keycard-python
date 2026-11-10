# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RoleAssignParams"]


class RoleAssignParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    owner_type: Literal["platform", "customer"]
    """Owner type of the role to assign.

    Required with role_identifier (an identifier is unique only per owner type);
    must be omitted with role_id.
    """

    role_id: str
    """ID of the role to assign.

    Provide exactly one of role_id or role_identifier; owner_type must be omitted
    when role_id is used.
    """

    role_identifier: str
    """
    Role identifier: a lowercase slug (letters and digits separated by single
    hyphens or underscores), unique per owner type within a zone. Role identifiers
    surface in policy evaluation, so the slug restriction keeps them unambiguous in
    policy text.
    """

    scope_id: str
    """The ID of the resource to scope the grant to.

    Provide together with scope_type, or omit both for an unscoped assignment. When
    scope_type is `zone`, this must reference a different zone in the same
    organization.
    """

    scope_type: str
    """The kind of resource to scope the grant to (e.g.

    `zone`). Provide together with scope_id, or omit both for an unscoped assignment
    (applies to the owning zone itself). Only platform roles on the org zone may
    carry a scope.
    """
