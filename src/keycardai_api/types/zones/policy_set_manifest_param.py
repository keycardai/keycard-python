# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .policy_set_manifest_entry_param import PolicySetManifestEntryParam

__all__ = ["PolicySetManifestParam"]


class PolicySetManifestParam(TypedDict, total=False):
    entries: Required[Iterable[PolicySetManifestEntryParam]]
