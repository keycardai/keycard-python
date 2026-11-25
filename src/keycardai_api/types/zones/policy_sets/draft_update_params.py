# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DraftUpdateParams", "ManifestOperation"]


class DraftUpdateParams(TypedDict, total=False):
    zone_id: Required[str]

    description: str

    manifest_operations: Iterable[ManifestOperation]

    name: str

    schema_version: str

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class ManifestOperation(TypedDict, total=False):
    op: Required[Literal["set", "add", "remove"]]
    """set: Replace policy_version_id for an existing entry matching policy_id.

    add: Append a new entry with the given policy_id and policy_version_id. remove:
    Remove the entry matching policy_id.
    """

    policy_id: Required[str]

    policy_version_id: str
    """Required for set and add operations. Ignored for remove."""
