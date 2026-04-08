# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .page_info_cursor import PageInfoCursor
from .organizations.organization_role import OrganizationRole

__all__ = ["OrganizationListIdentitiesResponse", "Item", "Pagination"]


class Item(BaseModel):
    """Unified view of users and invitations in an organization"""

    id: str
    """The identity ID (user or invitation)"""

    created_at: datetime
    """The time the entity was created in utc"""

    email: str
    """Email address of the identity"""

    role: OrganizationRole
    """Role in the organization"""

    source: str
    """Identity provider issuer"""

    status: Literal["active", "disabled", "pending", "accepted", "expired", "revoked"]
    """
    Status of the identity (OrganizationStatus for users, InvitationStatus for
    invitations)
    """

    type: Literal["user", "invitation"]
    """Type of identity (user or invitation)"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """


class Pagination(BaseModel):
    """Cursor-based pagination metadata returned alongside a list of results"""

    after_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    before_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    total_count: Optional[int] = None
    """Total number of items across all pages.

    Only present when the request includes ?expand=total_count.
    """


class OrganizationListIdentitiesResponse(BaseModel):
    """List of identities (users and invitations) in an organization"""

    items: List[Item]

    page_info: PageInfoCursor
    """Pagination information using cursor-based pagination"""

    pagination: Pagination
    """Cursor-based pagination metadata returned alongside a list of results"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """
