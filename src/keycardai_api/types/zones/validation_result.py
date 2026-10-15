# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ValidationResult", "Check"]


class Check(BaseModel):
    """Result of a single provider validation check"""

    check: Literal[
        "issuer_reachability",
        "metadata_retrieval",
        "endpoint_consistency",
        "authorization_endpoint_reachability",
        "credential_exchange",
    ]
    """Identifier of an individual provider validation check"""

    status: Literal["pass", "fail", "skipped_with_reason", "not_applicable"]
    """Outcome of a single check.

    `pass`/`fail` mean the check ran. `skipped_with_reason` means it could not run
    because a prerequisite is missing on our side (e.g. no credential stored).
    `not_applicable` means the check does not apply to this provider class (e.g. a
    login-flow-only provider that does not advertise the `client_credentials` grant)
    — render as a neutral state, distinct from a failure. Neither
    `skipped_with_reason` nor `not_applicable` fails the overall run.
    """

    detail: Optional[str] = None
    """
    Human-readable explanation, present on `fail`, `skipped_with_reason`, and
    `not_applicable`.
    """


class ValidationResult(BaseModel):
    """Result of running the provider OIDC connection checks on demand. Not persisted."""

    checks: List[Check]
    """Per-check results, in execution order"""

    provider_id: str
    """Provider that was validated"""

    status: Literal["pass", "fail"]
    """Overall outcome.

    `fail` when any individual check failed; skipped checks do not fail the run.
    """

    validated_at: datetime
    """When the validation run completed"""
