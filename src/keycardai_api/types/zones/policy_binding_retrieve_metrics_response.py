# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PolicyBindingRetrieveMetricsResponse", "Pairing"]


class Pairing(BaseModel):
    active_psv_id: str

    agree_count: int

    first_eval: datetime

    last_eval: datetime

    shadow_psv_id: str

    total: int


class PolicyBindingRetrieveMetricsResponse(BaseModel):
    agree_count: int

    shadow_allow_active_deny_count: int

    shadow_deny_active_allow_count: int

    since: datetime

    total_evaluations: int

    agreement_rate: Optional[float] = None
    """Fraction of evaluations where active and shadow decisions agreed (0.0–1.0)"""

    avg_shadow_duration_ms: Optional[int] = None

    pairings: Optional[List[Pairing]] = None
    """Per-pairing breakdown. Present when querying by PSV."""

    stddev_shadow_duration_ms: Optional[int] = None
