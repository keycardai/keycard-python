# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .metadata_param import MetadataParam

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """User specified identifier, unique within the zone"""

    name: Required[str]
    """Human-readable name"""

    application_id: str
    """ID of the application that provides this resource"""

    credential_provider_id: str
    """ID of the credential provider to associate with the resource"""

    description: Optional[str]
    """Human-readable description"""

    metadata: MetadataParam
    """Entity metadata"""

    scopes: SequenceNotStr[str]
    """Scopes supported by the resource"""
