# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .application_trait import ApplicationTrait

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    cursor: str

    identifier: str

    limit: int

    slug: str

    traits: List[ApplicationTrait]
    """
    Filter by traits (OR matching - returns applications with any of the specified
    traits)
    """

    traits_all: Annotated[List[ApplicationTrait], PropertyInfo(alias="traits[all]")]
    """
    Filter by traits (AND matching - returns applications with all of the specified
    traits)
    """
