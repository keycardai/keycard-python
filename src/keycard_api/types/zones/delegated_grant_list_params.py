# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DelegatedGrantListParams"]


class DelegatedGrantListParams(TypedDict, total=False):
    active: Literal["true"]

    resource_id: str
    """Filter by resource ID"""

    status: Literal["active", "expired", "revoked"]

    user_id: str
    """Filter by user ID"""
