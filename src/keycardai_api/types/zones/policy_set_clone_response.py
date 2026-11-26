# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .policy_set_with_binding import PolicySetWithBinding
from .policy_sets.policy_set_version import PolicySetVersion

__all__ = ["PolicySetCloneResponse", "Policy"]


class Policy(BaseModel):
    action: Literal["shared", "copied"]

    name: str
    """The pinned policy's name (the derived name when `copied`)."""

    policy_id: str
    """Public ID of the policy pinned by the clone.

    Equals `source_policy_id` when `shared`.
    """

    policy_version_id: str
    """Public ID of the pinned policy version. Equals the source's when `shared`."""

    source_policy_id: str
    """Public ID of the policy pinned by the source version."""


class PolicySetCloneResponse(BaseModel):
    policies: List[Policy]
    """One row per manifest entry, in manifest order."""

    policy_set: PolicySetWithBinding
    """The new set. `latest_version_id` is the first version; it is unbound."""

    policy_set_version: PolicySetVersion
    """The new set's first version, with manifest and attestation."""
