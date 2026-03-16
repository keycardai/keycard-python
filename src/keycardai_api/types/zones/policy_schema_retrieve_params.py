# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicySchemaRetrieveParams"]


class PolicySchemaRetrieveParams(TypedDict, total=False):
    zone_id: Required[str]

    format: Literal["cedar", "json"]
    """Schema representation format.

    `cedar` returns human-readable Cedar syntax in `cedar_schema`, `json` returns
    Cedar JSON schema object in `cedar_schema_json`.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
