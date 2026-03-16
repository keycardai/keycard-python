# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .policy_set_manifest_entry import PolicySetManifestEntry

__all__ = ["PolicySetManifest"]


class PolicySetManifest(BaseModel):
    entries: List[PolicySetManifestEntry]
