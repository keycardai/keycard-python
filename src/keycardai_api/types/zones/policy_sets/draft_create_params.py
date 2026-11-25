# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..policy_set_manifest_param import PolicySetManifestParam

__all__ = ["DraftCreateParams"]


class DraftCreateParams(TypedDict, total=False):
    zone_id: Required[str]

    base_version_id: str
    """ID of a policy set version to hydrate from.

    Mutually exclusive with manifest — the server rejects requests containing both
    fields.
    """

    description: str

    manifest: PolicySetManifestParam

    name: str

    schema_version: str

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
