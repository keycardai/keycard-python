# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .base_fields import BaseFields

__all__ = ["URL"]


class URL(BaseFields):
    """URL-based application credential"""

    identifier: str
    """URL of the credential (must be a valid URL)"""

    type: Literal["url"]
