# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
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
    """Maximum number of invitations to return"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]

    x_request_id: Annotated[str, PropertyInfo(alias="X-Request-ID")]
