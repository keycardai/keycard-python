# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ServiceAccountRetrieveParams"]


class ServiceAccountRetrieveParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID or label identifier"""

    expand: List[Literal["permissions"]]
    """Fields to expand in the response.

    Currently supports "permissions" to include the permissions field with the
    caller's permissions for the resource.
    """

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
