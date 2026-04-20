# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ..policy_set_manifest import PolicySetManifest
from ..attestation_statement import AttestationStatement

__all__ = ["PolicySetVersion"]


class PolicySetVersion(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    manifest: PolicySetManifest

    manifest_sha: str
    """Hex-encoded SHA-256 of the canonicalized manifest"""

    owner_type: Literal["platform", "customer"]
    """Who manages this policy set version:

    - `"platform"` — managed by the Keycard platform (system policy set versions).
    - `"customer"` — managed by the tenant (custom policy set versions).
    """

    policy_set_id: str

    schema_version: str
    """Schema version pinned to this policy set version.

    Determines the Cedar schema used for evaluation when activated.
    """

    version: int

    active: Optional[bool] = None
    """Whether this policy set version is currently bound with mode='active'"""

    archived_at: Optional[datetime] = None

    archived_by: Optional[str] = None

    attestation: Optional[AttestationStatement] = None
    """Decoded content of an Attestation JWS payload.

    Describes the exact policy set version composition at attestation time. This
    schema defines what consumers see after base64url-decoding the
    Attestation.payload field.
    """
