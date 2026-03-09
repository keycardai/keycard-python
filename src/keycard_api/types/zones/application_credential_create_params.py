# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ApplicationCredentialCreateParams",
    "IamApplicationCredentialCreateToken",
    "IamApplicationCredentialCreatePassword",
    "IamApplicationCredentialCreatePublicKey",
    "IamApplicationCredentialCreateURL",
    "IamApplicationCredentialCreatePublic",
]


class IamApplicationCredentialCreateToken(TypedDict, total=False):
    application_id: Required[str]
    """ID of the application this credential belongs to"""

    provider_id: Required[str]
    """ID of the provider issuing tokens this credential verifies"""

    type: Required[Literal["token"]]

    subject: str
    """Subject identifier for the token.

    When omitted, any token from the provider is accepted without checking
    application-specific claims.
    """


class IamApplicationCredentialCreatePassword(TypedDict, total=False):
    application_id: Required[str]
    """ID of the application this credential belongs to"""

    type: Required[Literal["password"]]

    identifier: str
    """
    Username for password credential, also used as OAuth 2.0 client ID
    (auto-generated if not provided)
    """


class IamApplicationCredentialCreatePublicKey(TypedDict, total=False):
    application_id: Required[str]
    """ID of the application this credential belongs to"""

    jwks_uri: Required[str]
    """JWKS URI to retrieve public keys from"""

    type: Required[Literal["public-key"]]

    identifier: str
    """
    Client ID for public key credential, also used as OAuth 2.0 client ID
    (auto-generated if not provided)
    """


class IamApplicationCredentialCreateURL(TypedDict, total=False):
    application_id: Required[str]
    """ID of the application this credential belongs to"""

    identifier: Required[str]
    """URL of the credential (must be a valid URL)"""

    type: Required[Literal["url"]]


class IamApplicationCredentialCreatePublic(TypedDict, total=False):
    application_id: Required[str]
    """ID of the application this credential belongs to"""

    type: Required[Literal["public"]]

    identifier: str
    """
    Identifier for public credential, also used as OAuth 2.0 client ID
    (auto-generated if not provided)
    """


ApplicationCredentialCreateParams: TypeAlias = Union[
    IamApplicationCredentialCreateToken,
    IamApplicationCredentialCreatePassword,
    IamApplicationCredentialCreatePublicKey,
    IamApplicationCredentialCreateURL,
    IamApplicationCredentialCreatePublic,
]
