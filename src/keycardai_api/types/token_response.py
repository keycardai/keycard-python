# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenResponse"]


class TokenResponse(BaseModel):
    """OAuth2-style token response for M2M tokens"""

    access_token: str
    """The M2M access token"""

    token_type: str
    """Token type (always "Bearer")"""

    expires_in: Optional[int] = None
    """Token expiration time in seconds"""
