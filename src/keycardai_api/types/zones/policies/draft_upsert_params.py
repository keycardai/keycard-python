# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DraftUpsertParams"]


class DraftUpsertParams(TypedDict, total=False):
    zone_id: Required[str]

    schema_version: Required[str]

    format: Literal["cedar", "json"]
    """Response format override.

    `json` returns cedar_json, `cedar` returns cedar_raw. When omitted, the response
    matches the input format.
    """

    validate_cedar: bool
    """Whether to validate cedar_json against the schema. Defaults to true."""

    cedar_json: Optional[object]
    """Cedar policy in JSON representation. Mutually exclusive with cedar_raw."""

    cedar_raw: Optional[str]
    """Cedar policy in human-readable Cedar syntax.

    Mutually exclusive with cedar_json.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
