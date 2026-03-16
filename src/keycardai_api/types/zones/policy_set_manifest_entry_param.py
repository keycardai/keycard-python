# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PolicySetManifestEntryParam"]


class PolicySetManifestEntryParam(TypedDict, total=False):
    policy_id: Required[str]

    policy_version_id: Required[str]

    sha: str
    """SHA-256 of the policy version content, populated by the server"""
