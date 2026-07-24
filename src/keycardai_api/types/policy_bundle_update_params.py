# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["PolicyBundleUpdateParams"]


class PolicyBundleUpdateParams(TypedDict, total=False):
    body: Required[FileTypes]
    """tar+gzip Policy Bundle archive.

    `manifest.json` is **required** (see `PolicyBundleManifest`);
    `schema.cedarschema` is **optional and ignored** — the server validates against
    its attested schema for `manifest.schema.version`. The manifest's `policies[]`
    list is authoritative for the resulting set: each entry must have a matching
    `policies/<public_id>.cedar` (or, for a `new_policy` entry,
    `policies/<new_policy>.cedar`) member, and a member with no manifest entry is
    dropped. Only the `sha` fields are advisory and recomputed server-side.
    Duplicate or unrecognized entries are rejected with `bundle_invalid`. See the
    **PolicyBundle** tag for the layout.
    """

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]
