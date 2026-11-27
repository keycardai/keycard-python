# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicyBindingRetrieveMetricsParams"]


class PolicyBindingRetrieveMetricsParams(TypedDict, total=False):
    zone_id: Required[str]

    policy_set_id: str
    """Policy set to filter metrics for. Required when psv_id is provided."""

    psv_id: str
    """Filter to a specific policy set version (in any role).

    When provided, response includes per-pairing breakdown. Requires policy_set_id.
    """

    scope: Literal["binding", "zone"]
    """Metrics scope.

    `binding` (default) returns metrics for this binding. `zone` returns zone-level
    aggregate across all pairings.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the time window (default 24h ago)"""

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
