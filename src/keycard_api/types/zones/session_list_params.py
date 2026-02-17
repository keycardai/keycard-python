# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    active: Literal["true"]

    session_type: Literal["user", "application"]

    status: Literal["active", "expired", "revoked"]

    user_id: str
    """Filter by user ID"""
