# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretListParams"]


class SecretListParams(TypedDict, total=False):
    entity_id: str
    """The entity to list all secrets for"""

    owner_type: Literal["platform", "customer"]
    """Filter by secret ownership.

    Services can select either owner type; other principals can select only
    customer-owned secrets. If omitted, services see both owner types and other
    principals see customer-owned secrets. Requires type=token or type=password when
    specified.
    """

    type: Literal["token", "password"]
    """The type of secrets to list. Required when owner_type is specified."""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
