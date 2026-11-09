# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RoleCreateParams"]


class RoleCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """
    Role identifier: a lowercase slug (letters and digits separated by single
    hyphens or underscores), unique per owner type within a zone. Role identifiers
    surface in policy evaluation, so the slug restriction keeps them unambiguous in
    policy text.
    """

    description: str
    """Human-readable description"""
