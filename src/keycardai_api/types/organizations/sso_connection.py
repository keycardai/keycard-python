# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .sso_connection_protocol import SSOConnectionProtocol

__all__ = ["SSOConnection"]


class SSOConnection(BaseModel):
    """SSO connection configuration for an organization"""

    id: str
    """Unique identifier for the SSO connection"""

    client_id: Optional[str] = None
    """OAuth 2.0 client ID"""

    client_secret_set: bool
    """Whether a client secret is configured"""

    created_at: datetime
    """The time the entity was created in utc"""

    identifier: str
    """SSO provider identifier (e.g., issuer URL)"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """

    protocols: Optional[SSOConnectionProtocol] = None
    """Protocol configuration for SSO connection"""
