# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..policy_set_manifest_entry import PolicySetManifestEntry

__all__ = ["ManifestRetrieveResponse"]


class ManifestRetrieveResponse(BaseModel):
    """
    Readback shape of a policy set version's manifest, richer than the write shape: each entry carries the resolved policy version ID and content SHA.
    """

    entries: List[PolicySetManifestEntry]

    policy_set_id: str

    manifest_sha: Optional[str] = None
    """JCS SHA-256 digest of the stored manifest of the returned version.

    Null when no versions exist yet. On the default latest read this is the same
    value the `ETag` header carries.
    """

    policy_set_version_id: Optional[str] = None
    """Null only for a policy set with no versions yet."""

    schema_version: Optional[str] = None
    """Null when no versions exist yet."""

    version: Optional[int] = None
    """Monotonic version number. Null when no versions exist yet."""
