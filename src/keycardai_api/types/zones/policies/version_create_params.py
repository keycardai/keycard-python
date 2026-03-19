# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionCreateParams"]


class VersionCreateParams(TypedDict, total=False):
    zone_id: Required[str]

    schema_version: Required[str]
    """Schema version to validate this policy against. Must not be archived."""

    cedar_json: Optional[object]
    """Cedar policy in JSON representation. Mutually exclusive with cedar_raw."""

    cedar_raw: Optional[str]
    """Cedar policy in human-readable Cedar syntax.

    Mutually exclusive with cedar_json.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
