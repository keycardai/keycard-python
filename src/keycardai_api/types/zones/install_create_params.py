# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InstallCreateParams"]


class InstallCreateParams(TypedDict, total=False):
    package_id: Required[str]
    """Public ID of the package to install."""

    inputs: Dict[str, object]
    """Parametric inputs required by the package."""

    version: int
    """Specific package version to install. Defaults to latest."""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
