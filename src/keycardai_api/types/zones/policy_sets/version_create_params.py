# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..policy_set_manifest_param import PolicySetManifestParam

__all__ = ["VersionCreateParams"]


class VersionCreateParams(TypedDict, total=False):
    zone_id: Required[str]

    manifest: Required[PolicySetManifestParam]

    schema_version: Required[str]
    """Schema version to pin to this policy set version."""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
