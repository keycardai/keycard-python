# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .base_fields import BaseFields

__all__ = ["PublicKey"]


class PublicKey(BaseFields):
    """Public key-based application credential"""

    identifier: str
    """Client ID for public key credential, also used as OAuth 2.0 client ID"""

    jwks_uri: str
    """JWKS URI to retrieve public keys from"""

    type: Literal["public-key"]
