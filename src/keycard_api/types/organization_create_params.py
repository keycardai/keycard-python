# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    name: str
    """Organization name"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
