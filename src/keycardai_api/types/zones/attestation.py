# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Attestation"]


class Attestation(BaseModel):
    """JWS Flattened JSON Serialization (RFC 7515 §7.2.2) of a policy set attestation.

    The protected header carries the signing algorithm and key identifier; the payload is a base64url-encoded AttestationStatement canonicalized per RFC 8785 (JCS). Verify using the zone JWKS endpoint (RFC 7517). Currently signed with RS256; future zone key types (e.g. EdDSA) will be indicated by the "alg" header — no envelope changes required.
    """

    payload: str
    """Base64url-encoded AttestationStatement (RFC 7515 §3).

    Decode to inspect attestation content. The RFC 8785 canonical form of the
    decoded JSON is the JWS Signing Input alongside the protected header.
    """

    protected: str
    """Base64url-encoded JWS protected header (RFC 7515 §4).

    Contains at minimum "alg" (signing algorithm — currently RS256, will migrate to
    EdDSA) and "kid" (signing key identifier resolvable via the zone JWKS endpoint).
    """

    signature: str
    """
    Base64url-encoded digital signature computed over the JWS Signing Input
    (ASCII(protected) || '.' || payload) per RFC 7515 §5.1.
    """
