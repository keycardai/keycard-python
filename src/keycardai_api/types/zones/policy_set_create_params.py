# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PolicySetCreateParams",
    "Manifest",
    "ManifestEntry",
    "ManifestEntryPdpExistingPolicyEntry",
    "ManifestEntryPdpNewPolicyEntry",
    "ManifestEntryPdpNewPolicyEntryNewPolicy",
]


class PolicySetCreateParams(TypedDict, total=False):
    name: Required[str]

    manifest: Manifest
    """Content for the first version, created atomically with the set."""

    scope_type: Literal["zone"]
    """**Deprecated.** Use `target_type` instead.

    Only `zone` is accepted; use `target_type` for `user` targets.
    """

    target_type: Literal["zone", "user"]
    """What this policy set targets:

    - `"zone"` — applies to all requests in the zone.
    - `"user"` — can be bound to a specific user.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class ManifestEntryPdpExistingPolicyEntry(TypedDict, total=False):
    """
    Reference to an existing (non-archived) policy in the zone — not limited to policies already in this set.
    With `cedar_raw`/`cedar_json` (mutually exclusive): the server diffs by content SHA; unchanged content under the resolved schema reuses the pinned policy version, changed content mints a new one.
    Without content ("pin as-is"): reuses the version pinned in the latest manifest, or the policy's latest version when the policy is newly added to this set. Bare pins are re-versioned when the resolved schema differs from the pinned version's schema.
    With `policy_version_id`: pins exactly that existing version and mints nothing. Mutually exclusive with `cedar_raw`/`cedar_json` (a version is content; 400 when both are supplied). The version must belong to `policy_id`, must not be archived (`version_archived`), and must have been validated against the resolved schema (`schema_version_mismatch`; no re-versioning). Reported as `repinned` when the set already pins a different version of the policy, otherwise `reused`.
    Platform-owned policies accept bare pins and `policy_version_id` (customers cannot mint versions of those).
    """

    policy_id: Required[str]
    """Public ID of an existing policy in the zone."""

    cedar_json: object
    """Cedar policy JSON. Mutually exclusive with cedar_raw."""

    cedar_raw: str
    """Cedar policy text. Mutually exclusive with cedar_json."""

    policy_version_id: str
    """Public ID of an existing version of `policy_id` to pin.

    Mutually exclusive with cedar_raw and cedar_json.
    """


class ManifestEntryPdpNewPolicyEntryNewPolicy(TypedDict, total=False):
    name: Required[str]

    description: str


class ManifestEntryPdpNewPolicyEntry(TypedDict, total=False):
    """
    Mints a new customer-owned policy with the requested name (409 `policy_name_conflict` on collision) plus its first version from the supplied content. Exactly one of `cedar_raw`/`cedar_json` is required.
    """

    new_policy: Required[ManifestEntryPdpNewPolicyEntryNewPolicy]

    cedar_json: object
    """Cedar policy JSON. Mutually exclusive with cedar_raw."""

    cedar_raw: str
    """Cedar policy text. Mutually exclusive with cedar_json."""


ManifestEntry: TypeAlias = Union[ManifestEntryPdpExistingPolicyEntry, ManifestEntryPdpNewPolicyEntry]


class Manifest(TypedDict, total=False):
    """Content for the first version, created atomically with the set."""

    entries: Required[Iterable[ManifestEntry]]
    """Initial manifest entries, in request order."""

    activate: bool
    """Bind the first version to the zone's active slot in the same transaction.

    Requires a zone-targeted set and the activate permission on policy_set_bindings.
    """

    schema_version: str
    """Schema to validate and pin v1 against. Defaults to the zone default."""
