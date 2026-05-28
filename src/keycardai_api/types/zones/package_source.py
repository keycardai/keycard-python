# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PackageSource"]


class PackageSource(BaseModel):
    """Provenance info for a package originating from an ancestor catalog."""

    scope: Literal["global", "org", "zone"]
    """Scope type of the catalog where the package is authored."""
