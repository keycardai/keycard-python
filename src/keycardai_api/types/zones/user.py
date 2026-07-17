# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .provider import Provider
from ..._models import BaseModel

__all__ = [
    "User",
    "Credential",
    "CredentialIamUserCredentialFederation",
    "CredentialIamUserCredentialPassword",
    "RoleAssignment",
    "RoleAssignmentScope",
]


class CredentialIamUserCredentialFederation(BaseModel):
    """Federation credential: the user authenticates through an identity provider."""

    created_at: datetime
    """Entity creation timestamp"""

    provider_id: Optional[str] = None
    """ID of the identity provider backing this credential.

    `null` when the source provider has been deleted.
    """

    type: Literal["federation"]

    updated_at: datetime
    """Entity update timestamp"""

    issuer: Optional[str] = None
    """Issuer identifier of the identity provider."""

    provider: Optional[Provider] = None
    """
    A Provider is a system that supplies access to Resources and allows actors
    (Users or Applications) to authenticate.
    """

    subject: Optional[str] = None
    """Subject identifier from the identity provider."""


class CredentialIamUserCredentialPassword(BaseModel):
    """Password credential: the user authenticates with email and password.

    The email lives on the user.
    """

    created_at: datetime
    """Entity creation timestamp"""

    type: Literal["password"]

    updated_at: datetime
    """Entity update timestamp"""


Credential: TypeAlias = Union[CredentialIamUserCredentialFederation, CredentialIamUserCredentialPassword]


class RoleAssignmentScope(BaseModel):
    """
    The resource this grant is scoped to, or null when the grant is unscoped (applies to the owning zone itself).
    """

    id: str
    """The ID of the scoped resource."""

    type: str
    """The kind of resource this grant is scoped to (e.g. `zone`)."""


class RoleAssignment(BaseModel):
    """A role granted to a user within a zone."""

    role_id: str
    """ID of the assigned role"""

    role_identifier: str
    """Opaque role identifier.

    Treated as an opaque identifier by the API and unique within a zone.
    """

    scope: Optional[RoleAssignmentScope] = None
    """
    The resource this grant is scoped to, or null when the grant is unscoped
    (applies to the owning zone itself).
    """


class User(BaseModel):
    """An authenticated user entity"""

    id: str
    """Unique identifier of the user"""

    created_at: datetime
    """Entity creation timestamp"""

    email: str
    """Email address of the user"""

    email_verified: bool
    """Whether the email address has been verified"""

    identifier: str
    """Zone-scoped user identifier.

    Defaults to the user's Keycard ID. When the provider has user_identifier_claim
    configured, the value is set from that claim at user creation time.
    """

    organization_id: str
    """Organization that owns this user"""

    status: Literal["active", "disabled"]
    """Status of the user. Disabled users cannot authenticate."""

    updated_at: datetime
    """Entity update timestamp"""

    zone_id: str
    """Zone this user belongs to"""

    authenticated_at: Optional[str] = None
    """Date when the user was last authenticated"""

    credentials: Optional[List[Credential]] = None
    """
    Authentication credentials for this user, each carrying its identity provider
    for federation credentials. Populated only when `expand[]=credentials` is set on
    the listing endpoint.
    """

    grant_count: Optional[int] = None
    """Delegated-grant count for this user.

    Populated only when `expand[]=grant_count` is set on the listing endpoint.
    """

    issuer: Optional[str] = None
    """Issuer identifier of the identity provider"""

    provider_id: Optional[str] = None
    """Reference to the identity provider.

    This field is undefined when the source identity provider is deleted but the
    user is not deleted.
    """

    role_assignments: Optional[List[RoleAssignment]] = None
    """Role grants for this user within the zone.

    Populated only when `expand[]=role-assignments` is set on the listing endpoint.
    """

    session_count: Optional[int] = None
    """Session count for this user.

    Populated only when `expand[]=session_count` is set on the listing endpoint.
    """

    subject: Optional[str] = None
    """Subject identifier from the identity provider"""
