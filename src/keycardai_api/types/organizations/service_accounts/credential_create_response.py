# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CredentialCreateResponse"]


class CredentialCreateResponse(BaseModel):
    """Service account credential with plaintext secret (only returned on creation)"""

    id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    client_id: str
    """The client ID for authentication"""

    client_secret: str
    """The client secret"""

    created_at: datetime
    """The time the entity was created in utc"""

    name: str
    """A name for the entity to be displayed in UI"""

    description: Optional[str] = None
    """Optional description of the credential"""
