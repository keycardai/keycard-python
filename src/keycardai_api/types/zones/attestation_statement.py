# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AttestationStatement"]


class AttestationStatement(BaseModel):
    """Decoded content of an Attestation JWS payload.

    Describes the exact policy set version composition at attestation time. This schema defines what consumers see after base64url-decoding the Attestation.payload field.
    """

    attested_at: datetime

    attested_by: str

    key_id: str
    """Key ID of the signing key used to produce the attestation signature.

    Matches the "kid" in the JWS protected header.
    """

    manifest_sha: str
    """SHA-256 of the policy set version manifest.

    Verifiers MUST check this matches the policy_set_version.manifest_sha to detect
    attestation/version mismatches.
    """

    policy_set_id: str

    policy_set_version: int

    status: Literal["created", "re_signed"]
    """Event that produced this attestation.

    "created" is the initial attestation at version creation; "re_signed" is a
    re-attestation after key rotation (same content, new signature).
    """

    type: Literal["policy_set_attestation"]
    """Statement type discriminator"""

    v: Literal[1]
    """Statement schema version"""

    zone_id: str
