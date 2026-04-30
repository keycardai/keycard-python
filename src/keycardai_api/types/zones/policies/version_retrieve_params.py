# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionRetrieveParams"]


class VersionRetrieveParams(TypedDict, total=False):
    zone_id: Required[str]

    policy_id: Required[str]

    format: Literal["cedar", "json"]
    """Narrows which Cedar representation the response includes.

    When omitted, both `cedar_json` and `cedar_raw` are populated. Pass `json` to
    receive only `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that
    don't care about payload size can skip this parameter.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
