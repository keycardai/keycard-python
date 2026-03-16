# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .metadata_param import MetadataParam

__all__ = ["ApplicationCreateParams", "Dependency", "Protocols", "ProtocolsOauth2"]


class ApplicationCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """User specified identifier, unique within the zone"""

    name: Required[str]
    """Human-readable name"""

    dependencies: Iterable[Dependency]
    """Dependencies of the application"""

    description: Optional[str]
    """Human-readable description"""

    metadata: MetadataParam
    """Entity metadata"""

    protocols: Protocols
    """Protocol-specific configuration for application creation"""


class Dependency(TypedDict, total=False):
    id: Required[str]
    """Resource identifier"""

    type: str


class ProtocolsOauth2(TypedDict, total=False):
    """OAuth 2.0 protocol configuration for application creation"""

    post_logout_redirect_uris: SequenceNotStr[str]
    """OAuth 2.0 post-logout redirect URIs for this application"""

    redirect_uris: SequenceNotStr[str]
    """OAuth 2.0 redirect URIs for this application"""


class Protocols(TypedDict, total=False):
    """Protocol-specific configuration for application creation"""

    oauth2: ProtocolsOauth2
    """OAuth 2.0 protocol configuration for application creation"""
