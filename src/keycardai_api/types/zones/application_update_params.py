# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .metadata_update_param import MetadataUpdateParam

__all__ = ["ApplicationUpdateParams", "Protocols", "ProtocolsOauth2"]


class ApplicationUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    consent: Literal["implicit", "required"]
    """Consent mode for the application.

    'implicit' means consent is automatically granted, 'required' means explicit
    user consent is needed.
    """

    description: Optional[str]
    """Human-readable description.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    identifier: str
    """User specified identifier, unique within the zone.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    metadata: Optional[MetadataUpdateParam]
    """Entity metadata (set to null or {} to remove metadata)"""

    name: str
    """Human-readable name.

    Must not contain HTML tags (e.g. `<script>`, `<div>`) or control characters.
    """

    protocols: Optional[Protocols]
    """Protocol-specific configuration for application update"""


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for application update"""

    post_logout_redirect_uris: Optional[SequenceNotStr[str]]
    """
    OAuth 2.0 post-logout redirect URIs for this application (set to null or [] to
    unset)
    """

    redirect_uris: Optional[SequenceNotStr[str]]
    """OAuth 2.0 redirect URIs for this application (set to null or [] to unset)"""


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration for application update"""

    oauth2: Optional[ProtocolsOauth2]
    """OAuth 2.0 protocol configuration for application update"""
