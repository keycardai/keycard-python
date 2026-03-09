# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretListParams"]


class SecretListParams(TypedDict, total=False):
    entity_id: str
    """The entity to list all secrets for"""

    type: Literal["token", "password"]
    """The type of secrets to list"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
