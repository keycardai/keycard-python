# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    cursor: str

    identifier: str

    limit: int

    slug: str

    type: Literal["external", "keycard-vault", "keycard-sts"]
