# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RoleAssignment"]


class RoleAssignment(BaseModel):
    """Represents a role assigned to a principal within a zone"""

    id: str
    """Unique identifier of the role assignment"""

    created_at: datetime
    """Entity creation timestamp"""

    principal_id: str
    """ID of the principal the role is assigned to (a user, application, or group ID)."""

    principal_type: str
    """The kind of principal the role is assigned to: `user`, `application`, or
    `group`.

    A role assigned to a `group` is inherited by that group's members.
    """

    role_id: str
    """ID of the assigned role"""

    role_identifier: str
    """
    Role identifier: a lowercase slug (letters and digits separated by single
    hyphens or underscores), unique per owner type within a zone. Role identifiers
    surface in policy evaluation, so the slug restriction keeps them unambiguous in
    policy text.
    """

    role_owner_type: Literal["platform", "customer"]
    """Owner type of the assigned role.

    Disambiguates roles that share an identifier across owner types.
    """

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this assignment belongs to"""

    scope_id: Optional[str] = None
    """The ID of the scoped resource. Null when the assignment is unscoped."""

    scope_type: Optional[str] = None
    """The kind of resource this grant is scoped to (e.g.

    `zone`). Null when the assignment is unscoped (applies to the owning zone
    itself).
    """
