# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PolicySetManifestEntry"]


class PolicySetManifestEntry(BaseModel):
    policy_id: str

    policy_version_id: str

    sha: Optional[str] = None
    """SHA-256 of the policy version content, populated by the server"""
