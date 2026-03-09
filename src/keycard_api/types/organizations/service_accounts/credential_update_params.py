# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID or label identifier"""

    service_account_id: Required[str]
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    description: str
    """Optional description of the credential"""

    name: str
    """Credential name"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
