# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .user import User
from ..._models import BaseModel
from .user_agent import UserAgent
from .application import Application

__all__ = [
    "Session",
    "IamUserSessionType",
    "IamUserSessionTypeMetadata",
    "IamApplicationSessionType",
    "IamApplicationSessionTypeMetadata",
]


class IamUserSessionTypeMetadata(BaseModel):
    """Session metadata"""

    name: str
    """Name of the initiating application or user agent"""


class IamUserSessionType(BaseModel):
    """User session type-specific fields"""

    session_type: Literal["user"]

    user_id: str
    """User ID"""

    id: Optional[str] = None
    """Session ID"""

    active: Optional[bool] = None
    """Whether the session is currently active (deprecated - use status instead)"""

    application: Optional[Application] = None
    """
    An Application is a software system with an associated identity that can access
    Resources. It may act on its own behalf (machine-to-machine) or on behalf of a
    user (delegated access).
    """

    application_id: Optional[str] = None
    """Application ID that initiated this session"""

    authenticated_at: Optional[datetime] = None
    """Date when the session was authenticated"""

    created_at: Optional[datetime] = None
    """Entity creation timestamp"""

    expires_at: Optional[datetime] = None
    """Date when session expires"""

    issuer: Optional[str] = None
    """Issuer URL from IdP"""

    metadata: Optional[IamUserSessionTypeMetadata] = None
    """Session metadata"""

    organization_id: Optional[str] = None
    """Organization that owns this session"""

    parent_id: Optional[str] = None
    """Parent session ID for hierarchical sessions (user sessions only).

    When null, this is a web session - a top-level session initiated directly by a
    user. When set, this is a child session derived from the parent, used for token
    refresh or delegation. Application sessions cannot have parents.
    """

    provider_id: Optional[str] = None
    """Provider ID"""

    session_data: Optional[Dict[str, object]] = None
    """
    Session claims data (ID token claims for users, application claims for
    applications)
    """

    status: Optional[Literal["active", "expired", "revoked"]] = None

    subject: Optional[str] = None
    """Subject claim from IdP"""

    updated_at: Optional[datetime] = None
    """Entity update timestamp"""

    user: Optional[User] = None
    """An authenticated user entity"""

    user_agent: Optional[UserAgent] = None
    """
    A User Agent represents a user agent (browser, desktop app, CLI tool) that can
    initiate user sessions via OAuth 2.0 Dynamic Client Registration.
    """

    user_agent_id: Optional[str] = None
    """User agent ID (browser/client) that initiated this session"""

    zone_id: Optional[str] = None
    """Zone this session belongs to"""


class IamApplicationSessionTypeMetadata(BaseModel):
    """Session metadata"""

    name: str
    """Name of the initiating application or user agent"""


class IamApplicationSessionType(BaseModel):
    """Application session type-specific fields"""

    application_id: str
    """Application ID that initiated this session"""

    issuer: str
    """Issuer URL from IdP"""

    provider_id: str
    """Provider ID"""

    session_type: Literal["application"]

    subject: str
    """Subject claim from IdP"""

    id: Optional[str] = None
    """Session ID"""

    active: Optional[bool] = None
    """Whether the session is currently active (deprecated - use status instead)"""

    application: Optional[Application] = None
    """
    An Application is a software system with an associated identity that can access
    Resources. It may act on its own behalf (machine-to-machine) or on behalf of a
    user (delegated access).
    """

    authenticated_at: Optional[datetime] = None
    """Date when the session was authenticated"""

    created_at: Optional[datetime] = None
    """Entity creation timestamp"""

    expires_at: Optional[datetime] = None
    """Date when session expires"""

    metadata: Optional[IamApplicationSessionTypeMetadata] = None
    """Session metadata"""

    organization_id: Optional[str] = None
    """Organization that owns this session"""

    session_data: Optional[Dict[str, object]] = None
    """
    Session claims data (ID token claims for users, application claims for
    applications)
    """

    status: Optional[Literal["active", "expired", "revoked"]] = None

    updated_at: Optional[datetime] = None
    """Entity update timestamp"""

    zone_id: Optional[str] = None
    """Zone this session belongs to"""


Session: TypeAlias = Union[IamUserSessionType, IamApplicationSessionType]
