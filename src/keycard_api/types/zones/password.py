# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .base_fields import BaseFields

__all__ = ["Password"]


class Password(BaseFields):
    """Password-based application credential"""

    identifier: str
    """Username for password credential, also used as OAuth 2.0 client ID"""

    type: Literal["password"]

    password: Optional[str] = None
    """
    Password for credential (only returned on creation, store securely), also used
    as OAuth 2.0 client secret
    """
