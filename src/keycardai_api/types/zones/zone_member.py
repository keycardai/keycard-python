# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .zone_role import ZoneRole

__all__ = ["ZoneMember", "_Links", "_LinksOrganizationUser", "_LinksSelf"]


class _LinksOrganizationUser(BaseModel):
    href: str
    """Link to the user resource"""


class _LinksSelf(BaseModel):
    href: str
    """Link to this zone member resource"""


class _Links(BaseModel):
    """HAL-format hypermedia links for zone member resources"""

    organization_user: _LinksOrganizationUser

    self: _LinksSelf


class ZoneMember(BaseModel):
    """Represents an organization user's membership in a zone with an assigned role"""

    id: str
    """Unique identifier of the zone member"""

    api_links: _Links = FieldInfo(alias="_links")
    """HAL-format hypermedia links for zone member resources"""

    created_at: datetime
    """Entity creation timestamp"""

    organization_id: str
    """Organization ID that owns the zone"""

    organization_user_id: str
    """Organization user ID of the zone member"""

    role: ZoneRole
    """Zone role type.

    zone_manager has full management access, zone_viewer has read-only access.
    """

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone ID the organization user is a member of"""
