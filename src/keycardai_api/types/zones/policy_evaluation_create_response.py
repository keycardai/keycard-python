# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "PolicyEvaluationCreateResponse",
    "Check",
    "CheckDeterminingPolicy",
    "Diagnostic",
    "EntitySnapshot",
    "EntitySnapshotPrincipal",
    "EntitySnapshotPrincipalPdpUserSnapshot",
    "EntitySnapshotPrincipalPdpApplicationSnapshot",
    "EntitySnapshotPrincipalPdpApplicationSnapshotDependency",
    "EntitySnapshotResource",
    "EntitySnapshotSubject",
    "EntitySnapshotSubjectPdpUserSnapshot",
    "EntitySnapshotSubjectPdpApplicationSnapshot",
    "EntitySnapshotSubjectPdpApplicationSnapshotDependency",
]


class CheckDeterminingPolicy(BaseModel):
    """
    A policy that contributed to the decision, enriched with human-readable
    names and version. For an allow these are permit policies; for an
    explicit deny these are forbid policies. An implicit (fall-through)
    deny has none. On the management test-evaluate endpoint, names and
    policy-set version populate only when a minted policy version is being
    evaluated; raw text and draft sources stay structural.
    """

    effect: Optional[Literal["permit", "forbid"]] = None

    policy_id: Optional[str] = None
    """Public ID of the policy."""

    policy_name: Optional[str] = None
    """Human-readable policy name."""

    policy_set_id: Optional[str] = None
    """Public ID of the policy set the policy belongs to."""

    policy_set_name: Optional[str] = None
    """Human-readable policy set name."""

    policy_set_version: Optional[int] = None
    """Version number of the policy set."""

    policy_version_id: Optional[str] = None
    """Public ID of the policy version that was evaluated."""

    rule_id: Optional[str] = None
    """Cedar per-rule `@id` annotation that determined the decision (e.g.

    `limit-linear-scopes`). Falls back to the generated `policyN` key when the Cedar
    statement carries no `@id`.
    """


class Check(BaseModel):
    """Result of a single Cedar sub-check within a compound evaluation.

    Each
    check's determining policies and their effect are attributed to that
    check's own decision, not the deny-wins aggregate.
    """

    decision: Optional[Literal["allow", "deny"]] = None

    determining_policies: Optional[List[CheckDeterminingPolicy]] = None

    role: Optional[Literal["actor", "subject"]] = None
    """
    actor = the requesting principal's access (or its right to act for the subject
    in an on-behalf-of flow); subject = the impersonated / delegated principal's own
    access.
    """


class Diagnostic(BaseModel):
    message: Optional[str] = None

    policy_id: Optional[str] = None


class EntitySnapshotPrincipalPdpUserSnapshot(BaseModel):
    """Subset of the IAM User entity relevant to Cedar evaluation.

    All fields match the IAM management API User schema.
    """

    id: str
    """User public ID (same as IAM management API)."""

    email: str

    type: Literal["user"]

    email_verified: Optional[bool] = None


class EntitySnapshotPrincipalPdpApplicationSnapshotDependency(BaseModel):
    """Subset of the IAM Resource entity relevant to Cedar evaluation.

    All fields match the IAM management API Resource schema.
    """

    id: str
    """Resource public ID (same as IAM management API)."""

    identifier: str

    name: str

    scopes: Optional[List[str]] = None


class EntitySnapshotPrincipalPdpApplicationSnapshot(BaseModel):
    """Subset of the IAM Application entity relevant to Cedar evaluation.

    All fields match the IAM management API Application schema.
    """

    id: str
    """Application public ID (same as IAM management API)."""

    name: str

    registration_method: Literal["managed", "dcr"]

    type: Literal["application"]

    credential_type: Optional[str] = None
    """Present only when resolved via credential lookup."""

    dependencies: Optional[List[EntitySnapshotPrincipalPdpApplicationSnapshotDependency]] = None
    """Resources this application depends on."""


EntitySnapshotPrincipal: TypeAlias = Union[
    EntitySnapshotPrincipalPdpUserSnapshot, EntitySnapshotPrincipalPdpApplicationSnapshot
]


class EntitySnapshotResource(BaseModel):
    """Subset of the IAM Resource entity relevant to Cedar evaluation.

    All fields match the IAM management API Resource schema.
    """

    id: str
    """Resource public ID (same as IAM management API)."""

    identifier: str

    name: str

    scopes: Optional[List[str]] = None


class EntitySnapshotSubjectPdpUserSnapshot(BaseModel):
    """Subset of the IAM User entity relevant to Cedar evaluation.

    All fields match the IAM management API User schema.
    """

    id: str
    """User public ID (same as IAM management API)."""

    email: str

    type: Literal["user"]

    email_verified: Optional[bool] = None


class EntitySnapshotSubjectPdpApplicationSnapshotDependency(BaseModel):
    """Subset of the IAM Resource entity relevant to Cedar evaluation.

    All fields match the IAM management API Resource schema.
    """

    id: str
    """Resource public ID (same as IAM management API)."""

    identifier: str

    name: str

    scopes: Optional[List[str]] = None


class EntitySnapshotSubjectPdpApplicationSnapshot(BaseModel):
    """Subset of the IAM Application entity relevant to Cedar evaluation.

    All fields match the IAM management API Application schema.
    """

    id: str
    """Application public ID (same as IAM management API)."""

    name: str

    registration_method: Literal["managed", "dcr"]

    type: Literal["application"]

    credential_type: Optional[str] = None
    """Present only when resolved via credential lookup."""

    dependencies: Optional[List[EntitySnapshotSubjectPdpApplicationSnapshotDependency]] = None
    """Resources this application depends on."""


EntitySnapshotSubject: TypeAlias = Union[
    EntitySnapshotSubjectPdpUserSnapshot, EntitySnapshotSubjectPdpApplicationSnapshot
]


class EntitySnapshot(BaseModel):
    context: Optional[object] = None
    """The assembled Cedar context record."""

    principal: Optional[EntitySnapshotPrincipal] = None
    """Subset of the IAM User entity relevant to Cedar evaluation.

    All fields match the IAM management API User schema.
    """

    resource: Optional[EntitySnapshotResource] = None
    """Subset of the IAM Resource entity relevant to Cedar evaluation.

    All fields match the IAM management API Resource schema.
    """

    subject: Optional[EntitySnapshotSubject] = None
    """Present when subject_type/subject_id were provided."""


class PolicyEvaluationCreateResponse(BaseModel):
    decision: Literal["allow", "deny"]

    evaluated_at: datetime

    checks: Optional[List[Check]] = None
    """
    Per-sub-check results, each with the policies that determined it. A simple
    request has one actor check; an on-behalf-of / impersonation request has a
    subject check and an actor check. The overall decision is deny-wins across
    these. Determining-policy names and policy-set version populate only when
    evaluating a minted policy set/version; raw text and drafts are structural.
    """

    determining_policies: Optional[List[str]] = None
    """
    Raw Cedar policy IDs that determined the decision, of the form
    "<policy_version_id>::<cedar_key>", unioned across sub-checks. See `checks` for
    the resolved, human-readable form with per-check attribution.
    """

    diagnostics: Optional[List[Diagnostic]] = None

    entity_snapshot: Optional[EntitySnapshot] = None

    evaluation_status: Optional[Literal["complete", "partial"]] = None

    reason: Optional[str] = None
    """
    Human-readable explanation of the decision, suitable for presenting to end
    users.
    """
