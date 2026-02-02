# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .base_fields import BaseFields

__all__ = ["Public"]


class Public(BaseFields):
    """Public credential (no secret storage)"""

    identifier: str
    """Identifier for public credential, also used as OAuth 2.0 client ID"""

    type: Literal["public"]
