# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .provider import Provider
from .base_fields import BaseFields

__all__ = ["Token"]


class Token(BaseFields):
    """Token-based application credential"""

    identifier: str
    """Identifier for this credential.

    For version 2, this equals the credential ID and is the OAuth 2.0 client ID the
    workload sends. For version 1, this equals the subject value, or '\\**' when
    subject is not specified.
    """

    provider_id: str
    """ID of the provider issuing tokens verified by this credential"""

    type: Literal["token"]

    allowed_audience: Optional[str] = None
    """Version 2 only.

    Audience the token's `aud` must contain. `null` when unset, in which case the
    zone's issuer URL is required.
    """

    authentication_condition: Optional[str] = None
    """Version 2 only.

    CEL predicate over the token's `claims` that must evaluate to true. `null` when
    unset.
    """

    provider: Optional[Provider] = None
    """
    A Provider is a system that supplies access to Resources and allows actors
    (Users or Applications) to authenticate.
    """

    subject: Optional[str] = None
    """Subject identifier for the token.

    When null or omitted, any token from the provider is accepted without checking
    application-specific claims.
    """

    version: Optional[Literal[1, 2]] = None
    """Credential behavior version."""
