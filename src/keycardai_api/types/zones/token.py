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

    For token type, this equals the subject value, or '\\**' when subject is not
    specified.
    """

    provider_id: str
    """ID of the provider issuing tokens verified by this credential"""

    type: Literal["token"]

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
