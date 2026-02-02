# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ZoneListParams"]


class ZoneListParams(TypedDict, total=False):
    cursor: str

    limit: int

    slug: str
