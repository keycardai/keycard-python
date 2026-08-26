# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    """A zone-scoped group of users, assignable to roles and usable in policies.

    Roles assigned to a group are inherited by its members. `external` is false for groups managed in Keycard and true for groups synced from an external directory.
    """

    id: str
    """Unique identifier of the group"""

    created_at: datetime
    """Entity creation timestamp"""

    external: bool
    """Whether the group is synced from an external directory.

    When true the group is directory-owned and its membership is read-only; when
    false it is managed in Keycard. Read-only: set by external sync, never by the
    caller.
    """

    identifier: str
    """User-specified identifier, unique within the zone.

    Automatically assigned for groups from an external directory.
    """

    name: str
    """Human-readable group name"""

    organization_id: str
    """Organization this group belongs to"""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this group belongs to"""

    member_count: Optional[int] = None
    """Number of users in the group.

    Included only when requested via `expand[]=member_count` (group get or list).
    """

    roles: Optional[List[str]] = None
    """Identifiers of the roles assigned to the group; members inherit them.

    Deduped across scopes. Included only when requested via `expand[]=roles` (group
    get or list).
    """
