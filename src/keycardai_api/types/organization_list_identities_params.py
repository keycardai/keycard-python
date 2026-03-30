# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .organizations.organization_role import OrganizationRole

__all__ = ["OrganizationListIdentitiesParams"]


class OrganizationListIdentitiesParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination"""

    before: str
    """Cursor for backward pagination"""

    expand: List[Literal["permissions"]]
    """Fields to expand in the response.

    Currently supports "permissions" to include the permissions field with the
    caller's permissions for the resource.
    """

    limit: int
    """Maximum number of identities to return"""

    query_email: Annotated[str, PropertyInfo(alias="query[email]")]
    """Search identities by email substring (case-insensitive)"""

    role: OrganizationRole
    """Filter identities by role"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
