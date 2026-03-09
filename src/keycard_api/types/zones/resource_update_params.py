# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .metadata_update_param import MetadataUpdateParam

__all__ = ["ResourceUpdateParams"]


class ResourceUpdateParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    application_id: Optional[str]
    """ID of the application that provides this resource (set to null to unset)"""

    credential_provider_id: Optional[str]
    """
    ID of the credential provider to associate with the resource (set to null to
    unset)
    """

    description: Optional[str]
    """Human-readable description"""

    identifier: str
    """User specified identifier, unique within the zone"""

    metadata: Optional[MetadataUpdateParam]
    """Entity metadata (set to null or {} to remove metadata)"""

    name: str
    """Human-readable name"""

    scopes: Optional[SequenceNotStr[str]]
    """Scopes supported by the resource (set to null to unset)"""
