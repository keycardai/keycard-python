# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CredentialRetrieveParams"]


class CredentialRetrieveParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID or label identifier"""

    service_account_id: Required[str]
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    expand: Annotated[
        Union[Literal["permissions", "total_count"], List[Literal["permissions", "total_count"]]],
        PropertyInfo(alias="expand[]"),
    ]
    """Fields to expand in the response.

    Supports "permissions" to include the permissions field with the caller's
    permissions for the resource. For the service account and service account
    credential list operations, "total_count" populates pagination.total_count with
    the number of items matching the same filters as the list (excluding cursor and
    limit). Other operations ignore expand values they do not use.
    """

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
