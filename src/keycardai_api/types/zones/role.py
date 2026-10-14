# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    """A role that can be assigned to users within a zone."""

    id: str
    """Unique identifier of the role"""

    created_at: datetime
    """Entity creation timestamp"""

    identifier: str
    """
    Role identifier: a lowercase slug (letters and digits separated by single
    hyphens or underscores), unique per owner type within a zone. Role identifiers
    surface in policy evaluation, so the slug restriction keeps them unambiguous in
    policy text.
    """

    owner_type: Literal["platform", "customer"]
    """Who owns this role.

    Platform-owned roles are managed by Keycard and cannot be modified or deleted
    via the API; customer-owned roles are user-created.
    """

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this role belongs to"""

    description: Optional[str] = None
    """Human-readable description"""
