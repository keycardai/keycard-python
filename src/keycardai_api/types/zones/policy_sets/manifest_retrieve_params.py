# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ManifestRetrieveParams"]


class ManifestRetrieveParams(TypedDict, total=False):
    zone_id: Required[str]

    version: str
    """Policy set version public ID. Default: latest non-archived version."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
