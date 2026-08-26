# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable group name"""

    identifier: str
    """User-specified identifier, unique within the zone.

    Derived from the name when omitted (a suffix is appended if it collides).
    """
