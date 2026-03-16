# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ..attestation import Attestation
from ..policy_set_manifest import PolicySetManifest

__all__ = ["PolicySetVersion"]


class PolicySetVersion(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    manifest: PolicySetManifest

    manifest_sha: str
    """Hex-encoded SHA-256 of the canonicalized manifest"""

    policy_set_id: str

    schema_version: str

    version: int

    active: Optional[bool] = None
    """Whether this policy set version is currently bound with mode='active'"""

    archived_at: Optional[datetime] = None

    archived_by: Optional[str] = None

    attestation: Optional[Attestation] = None
    """JWS Flattened JSON Serialization (RFC 7515 §7.2.2) of a policy set attestation.

    The protected header carries the signing algorithm and key identifier; the
    payload is a base64url-encoded AttestationStatement canonicalized per RFC 8785
    (JCS). Verify using the zone JWKS endpoint (RFC 7517). Currently signed with
    RS256; future zone key types (e.g. EdDSA) will be indicated by the "alg" header
    — no envelope changes required.
    """
