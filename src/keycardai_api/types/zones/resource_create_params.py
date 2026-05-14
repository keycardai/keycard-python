# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .metadata_param import MetadataParam

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """User specified identifier, unique within the zone.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    name: Required[str]
    """Human-readable name.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    application_id: str
    """ID of the application that provides this resource"""

    application_type: Literal["native", "web"]
    """The expected type of client for this credential.

    Native clients must use localhost URLs for redirect_uris or URIs with custom
    schemes. Web clients must use https URLs and must not use localhost as the
    hostname.
    """

    credential_provider_id: str
    """ID of the credential provider to associate with the resource"""

    description: Optional[str]
    """Human-readable description.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    metadata: MetadataParam
    """Entity metadata"""

    prefix: bool
    """
    When true, the resource identifier is treated as a URI prefix and protects all
    URLs that share the identifier as a prefix. Defaults to false: resources only
    match by exact identifier unless explicitly enabled.
    """

    scopes: SequenceNotStr[str]
    """Scopes supported by the resource"""
