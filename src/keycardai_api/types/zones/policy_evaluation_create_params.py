# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .policy_set_manifest_entry_param import PolicySetManifestEntryParam

__all__ = [
    "PolicyEvaluationCreateParams",
    "PolicySource",
    "PolicySourceManifest",
    "PolicySourcePolicy",
    "PolicySourcePolicySet",
    "PolicySourceRaw",
    "Context",
    "ContextClaims",
    "ContextClaimsActingPrincipal",
    "ContextClaimsActor",
    "ContextClaimsSubject",
]


class PolicyEvaluationCreateParams(TypedDict, total=False):
    action: Required[str]
    """Cedar action to evaluate (e.g.

    `any`). The engine namespaces actions automatically as
    `Keycard::Action::"<name>"`.
    """

    policy_source: Required[PolicySource]
    """Specifies which policies to evaluate.

    Exactly one of policy, policy_set, raw, or manifest must be provided.
    """

    principal_id: Required[str]
    """Public ID of the user or application."""

    principal_type: Required[Literal["user", "application"]]

    resource_id: Required[str]
    """Public ID of the resource."""

    acting_principal_id: str
    """
    ID of the acting application from a verified RFC 8693 `actor_token`, as sent on
    `/policy/check`. Resolved with the same entity lookup as an application
    `principal_id` and exposed to Cedar as `context.acting_principal.application` on
    both checks. Lets a captured evaluation request be replayed faithfully.
    """

    authority_type: Optional[Literal["delegation", "impersonation"]]
    """Discriminator for the subject authority model.

    Determines how the subject relationship is expressed in the Cedar context:

    - `"delegation"` — sets `context.on_behalf = true` on the actor check. The actor
      is acting on behalf of the subject.
    - `"impersonation"` — sets `context.impersonate = true` on the actor check. The
      actor is impersonating the subject. When null and a subject is present,
      defaults to `"delegation"` for backward compatibility.
    """

    context: Context
    """Additional context for Cedar authorization evaluation.

    Fields here are mapped directly into the Cedar `context` record.
    """

    subject_id: str
    """Public ID of the subject (required when subject_type is set)."""

    subject_type: Literal["user", "application"]

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class PolicySourceManifest(TypedDict, total=False):
    """Inline policy-set manifest used by the `manifest` variant of PolicySource.

    Mirrors the shape of a stored policy set version's manifest so a policy set under construction (no stored id/version) can be tested without being saved first. The `sha` field on each entry is ignored on input and recomputed server-side.
    """

    entries: Required[Iterable[PolicySetManifestEntryParam]]

    schema_version: Required[str]
    """Cedar schema version the entries are validated against."""


class PolicySourcePolicy(TypedDict, total=False):
    policy_id: Required[str]
    """Public ID of the policy."""

    schema_version: str
    """Cedar schema version override (date string, e.g.

    "2026-03-16"). When omitted, uses the schema_version recorded on the resolved
    policy version or draft.
    """

    version_id: str
    """Public ID of a specific policy version.

    When omitted, the draft is used. If no draft exists, returns 400.
    """


class PolicySourcePolicySet(TypedDict, total=False):
    policy_set_id: Required[str]
    """Public ID of the policy set."""

    version_id: str
    """Public ID of a specific policy set version.

    When omitted, the draft is used. If no draft exists, returns 400.
    """


class PolicySourceRaw(TypedDict, total=False):
    cedar: Required[str]
    """Raw Cedar policy text.

    Can contain one or more policy statements. Converted to JSON before evaluation.
    """

    schema_version: Required[str]
    """Cedar schema version to evaluate against."""

    validate: bool
    """When true, validate the converted policy against the schema before evaluation.

    Validation errors are returned as 400 with details. Set to false to skip
    validation and attempt evaluation directly.
    """


class PolicySource(TypedDict, total=False):
    """Specifies which policies to evaluate.

    Exactly one of policy, policy_set, raw, or manifest must be provided.
    """

    manifest: PolicySourceManifest
    """Inline policy-set manifest used by the `manifest` variant of PolicySource.

    Mirrors the shape of a stored policy set version's manifest so a policy set
    under construction (no stored id/version) can be tested without being saved
    first. The `sha` field on each entry is ignored on input and recomputed
    server-side.
    """

    policy: PolicySourcePolicy

    policy_set: PolicySourcePolicySet

    raw: PolicySourceRaw


class ContextClaimsActingPrincipal(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: str
    """Email claim from the authentication token."""

    groups: SequenceNotStr[str]
    """Group membership claims from the authentication token."""

    issuer_claims: Dict[str, object]
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """


class ContextClaimsActor(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: str
    """Email claim from the authentication token."""

    groups: SequenceNotStr[str]
    """Group membership claims from the authentication token."""

    issuer_claims: Dict[str, object]
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """


class ContextClaimsSubject(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Represents token claims passed into the Cedar context.

    Mapped to the
    Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as
    untyped key-value pairs via `additionalProperties`.
    """

    email: str
    """Email claim from the authentication token."""

    groups: SequenceNotStr[str]
    """Group membership claims from the authentication token."""

    issuer_claims: Dict[str, object]
    """Issuer-specific claims forwarded opaquely from STS (e.g.

    GHA OIDC assertion claims). Mapped to `context.actor_claims.issuer_claims` in
    Cedar. All fields are optional and issuer-dependent. See issuer documentation
    for available claim fields.
    """


class ContextClaims(TypedDict, total=False):
    """Token claims for the actor, subject, and/or acting principal.

    Mapped to
    `context.actor_claims`, `context.subject_claims`, and
    `context.acting_principal_claims` in Cedar.
    """

    acting_principal: ContextClaimsActingPrincipal
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """

    actor: ContextClaimsActor
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """

    subject: ContextClaimsSubject
    """Represents token claims passed into the Cedar context.

    Mapped to the Cedar `Keycard::Claims` type. Known fields (`email`, `groups`,
    `issuer_claims`) are typed; additional claims are passed through as untyped
    key-value pairs via `additionalProperties`.
    """


class Context(TypedDict, total=False):
    """Additional context for Cedar authorization evaluation.

    Fields here
    are mapped directly into the Cedar `context` record.
    """

    claims: ContextClaims
    """Token claims for the actor, subject, and/or acting principal.

    Mapped to `context.actor_claims`, `context.subject_claims`, and
    `context.acting_principal_claims` in Cedar.
    """

    scopes: SequenceNotStr[str]
    """OAuth scopes associated with the request.

    Mapped to `context.scopes` in the Cedar evaluation as a `Set<String>`.
    """

    session_id: str
    """Session identifier for the current authorization context.

    Mapped to `context.session_id` in Cedar.
    """
