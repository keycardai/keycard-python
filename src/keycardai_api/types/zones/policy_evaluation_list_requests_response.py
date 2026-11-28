# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PolicyEvaluationListRequestsResponse",
    "Item",
    "ItemContext",
    "ItemContextClaims",
    "ItemContextClaimsActingPrincipal",
    "ItemContextClaimsActor",
    "ItemContextClaimsSubject",
    "Pagination",
]


class ItemContextClaimsActingPrincipal(BaseModel):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: Optional[str] = None
    """Email claim from the authentication token."""

    groups: Optional[List[str]] = None
    """Group membership claims from the authentication token."""

    issuer_claims: Optional[Dict[str, object]] = None
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ItemContextClaimsActor(BaseModel):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: Optional[str] = None
    """Email claim from the authentication token."""

    groups: Optional[List[str]] = None
    """Group membership claims from the authentication token."""

    issuer_claims: Optional[Dict[str, object]] = None
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ItemContextClaimsSubject(BaseModel):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: Optional[str] = None
    """Email claim from the authentication token."""

    groups: Optional[List[str]] = None
    """Group membership claims from the authentication token."""

    issuer_claims: Optional[Dict[str, object]] = None
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ItemContextClaims(BaseModel):
    """Token claims for the actor, subject, and/or acting principal.

    Mapped to
    `context.actor_claims`, `context.subject_claims`, and
    `context.acting_principal_claims` in Cedar.
    """

    acting_principal: Optional[ItemContextClaimsActingPrincipal] = None
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """

    actor: Optional[ItemContextClaimsActor] = None
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """

    subject: Optional[ItemContextClaimsSubject] = None
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """


class ItemContext(BaseModel):
    """Additional context for Cedar authorization evaluation.

    Fields here
    are mapped directly into the Cedar `context` record.
    """

    claims: Optional[ItemContextClaims] = None
    """Token claims for the actor, subject, and/or acting principal.

    Mapped to `context.actor_claims`, `context.subject_claims`, and
    `context.acting_principal_claims` in Cedar.
    """

    scopes: Optional[List[str]] = None
    """OAuth scopes associated with the request.

    Mapped to `context.scopes` in the Cedar evaluation as a `Set<String>`.
    """

    session_id: Optional[str] = None
    """Session identifier for the current authorization context.

    Mapped to `context.session_id` in Cedar.
    """


class Item(BaseModel):
    id: str
    """Unique identifier for this evaluation request entry."""

    action: str

    active_decision: Literal["allow", "deny"]

    active_duration_ms: int
    """Evaluation duration in milliseconds."""

    active_psv_id: str
    """ID of the active policy set version used for evaluation."""

    active_schema_version: str
    """Cedar schema version of the active policy set version."""

    created_at: datetime

    principal_id: str

    principal_type: Literal["user", "application"]

    request_id: str
    """Correlation ID from the original credentials API request."""

    resource_id: str

    acting_principal_id: Optional[str] = None
    """
    The verified RFC 8693 acting principal (nominated via actor_token) from the
    original check, when one was present.
    """

    authority_type: Optional[Literal["delegation", "impersonation"]] = None

    context: Optional[ItemContext] = None
    """Additional context for Cedar authorization evaluation.

    Fields here are mapped directly into the Cedar `context` record.
    """

    shadow_psv_id: Optional[str] = None
    """ID of the shadow policy set version, if a shadow binding existed."""

    subject_id: Optional[str] = None

    subject_type: Optional[Literal["user", "application"]] = None


class Pagination(BaseModel):
    """Cursor-based pagination metadata returned alongside a list of results"""

    after_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    before_cursor: Optional[str] = None
    """An opaque cursor used for paginating through a list of results"""

    total_count: Optional[int] = None
    """Total number of items across all pages.

    Only present when the request includes ?expand[]=total_count.
    """


class PolicyEvaluationListRequestsResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
    """Cursor-based pagination metadata returned alongside a list of results"""
