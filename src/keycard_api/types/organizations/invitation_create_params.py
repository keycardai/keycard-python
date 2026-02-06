# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    email: Required[str]
    """Email address to invite"""

    role: Literal["org_admin", "org_member", "org_viewer"]
    """
    Role to assign when invitation is accepted (defaults to org_admin if not
    provided)
    """

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
