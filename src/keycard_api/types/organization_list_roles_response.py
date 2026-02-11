# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .role_scope import RoleScope

__all__ = ["OrganizationListRolesResponse", "Item"]


class Item(BaseModel):
    """A role definition that can be assigned to users"""

    description: str
    """Detailed description of the role and its permissions"""

    label: str
    """Human-readable display name for the role"""

    name: str
    """Internal identifier for the role (e.g., org_admin, zone_manager)"""

    scope: RoleScope
    """The scope at which this role can be assigned (organization or zone)"""


class OrganizationListRolesResponse(BaseModel):
    """List of available roles"""

    items: List[Item]
    """List of roles"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
