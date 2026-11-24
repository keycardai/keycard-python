# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "ManifestApplyParams",
    "Entry",
    "EntryPdpExistingPolicyEntry",
    "EntryPdpNewPolicyEntry",
    "EntryPdpNewPolicyEntryNewPolicy",
]


class ManifestApplyParams(TypedDict, total=False):
    zone_id: Required[str]

    entries: Required[Iterable[Entry]]
    """Complete desired content.

    Order is preserved for newly added policies; retained policies keep their
    current manifest order (so an unchanged apply reproduces the identical manifest
    and dedups).
    """

    dry_run: bool
    """Not yet implemented — `true` returns 501 until ACC-1002.

    When true, performs validation, schema resolution, and the content diff, and
    returns the would-be `changes` and `warnings` — but persists nothing.
    `policy_set_version` is omitted from the response and no ETag is returned.
    """

    activate: bool
    """
    Also rebind the zone/active slot to the resulting version in the same
    transaction. Requires the `activate` permission on policy set bindings. Targets
    only the zone/active slot; other slots go through PUT /policy-bindings.
    """

    schema_version: str
    """Cedar schema version to validate and pin the resulting version against.

    Omitted: the server resolves it (latest version's schema if still writable, else
    the zone default).
    """

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class EntryPdpExistingPolicyEntry(TypedDict, total=False):
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


class EntryPdpNewPolicyEntryNewPolicy(TypedDict, total=False):
    name: Required[str]

    description: str


class EntryPdpNewPolicyEntry(TypedDict, total=False):
    """
    Mints a new customer-owned policy with the requested name (409 `policy_name_conflict` on collision) plus its first version from the supplied content. Exactly one of `cedar_raw`/`cedar_json` is required.
    """

    new_policy: Required[EntryPdpNewPolicyEntryNewPolicy]

    cedar_json: object
    """Cedar policy JSON. Mutually exclusive with cedar_raw."""

    cedar_raw: str
    """Cedar policy text. Mutually exclusive with cedar_json."""


Entry: TypeAlias = Union[EntryPdpExistingPolicyEntry, EntryPdpNewPolicyEntry]
