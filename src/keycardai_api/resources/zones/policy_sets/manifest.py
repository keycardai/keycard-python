# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zones.policy_sets import manifest_apply_params, manifest_retrieve_params
from ....types.zones.policy_sets.manifest_apply_response import ManifestApplyResponse
from ....types.zones.policy_sets.manifest_retrieve_response import ManifestRetrieveResponse

__all__ = ["ManifestResource", "AsyncManifestResource"]


class ManifestResource(SyncAPIResource):
    """Declarative read/apply of a policy set's full content"""

    @cached_property
    def with_raw_response(self) -> ManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return ManifestResourceWithStreamingResponse(self)

    def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestRetrieveResponse:
        """
        Returns the resolved manifest of the **latest non-archived version** by default.
        Pass `?version=` with a policy set version public ID to read a specific
        version's manifest (e.g. for rollback: GET an old manifest, PUT it back — which
        mints a new version at the tip with the old content; history is never
        re-pointed).

        There is deliberately no `?version=active` keyword: a binding slot is
        `(zone, target_type, target_id, mode)` and a set may have zero or several active
        bindings, so "the active version" is not a function of the set alone. Resolve
        the version ID first — from the enriched policy set representation
        (`active_version_id`) or `GET /policy-bindings` — then pass it here.

        The default (latest) read anchors the apply flow: the `ETag` response header is
        the JCS SHA-256 digest of the latest manifest and is the value to send as
        `If-Match` on `PUT`. **`ETag` is emitted only on the default latest read** —
        versioned reads return `manifest_sha` in the body but no `ETag`, so a stale
        token cannot be round-tripped as a precondition.

        A policy set with no versions yet returns `200` with empty `entries`, null
        `policy_set_version_id`/`version`/`schema_version`/`manifest_sha`, and the
        digest of the empty manifest as `ETag`, so even the first apply can be
        conditional.

        Args:
          version: Policy set version public ID. Default: latest non-archived version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/manifest", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, manifest_retrieve_params.ManifestRetrieveParams),
            ),
            cast_to=ManifestRetrieveResponse,
        )

    def apply(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        entries: Iterable[manifest_apply_params.Entry],
        dry_run: bool | Omit = omit,
        activate: bool | Omit = omit,
        schema_version: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestApplyResponse:
        """Declarative full-replace apply.

        `entries` is the complete desired content of the
        policy set: **any policy omitted from `entries` is dropped from the resulting
        version** (its rows are retained and a later apply may reference it again).
        Entry order is preserved for newly added policies; retained policies keep their
        current manifest order, so an unchanged apply is byte-identical and dedups to
        the existing version.

        Per entry, the server diffs by content SHA against the version pinned in the
        latest manifest: unchanged content under the same schema version reuses the
        pinned policy version; changed content mints a new policy version; `new_policy`
        entries mint a customer-owned policy with the requested name. All of this, plus
        the policy set version mint and the optional activation, happens in **one
        transaction** (row lock on the policy set). Cedar validation runs against the
        resolved schema before the transaction opens — an invalid policy rejects the
        whole apply with zero writes.

        **Schema resolution:** `schema_version` omitted → the latest version's schema if
        still writable, else the zone default. Provided → authoritative
        (`schema_version_unsupported` if unknown, unattested, or archived). All entries
        validate against the single resolved version (uniform-schema-per-version is
        retained); a pinned policy version created under a different schema is
        re-versioned even if its content is unchanged.

        **Activation:** `activate: true` requires a zone-targeted set and rebinds the
        `(zone, target_type=zone, mode=active)` slot to the resulting version in the
        same transaction. It requires `policy_set_bindings:activate` permission and
        preserves the previous binding in binding history. Unchanged content returns
        `created: false` and still activates the resulting version. An already active
        version keeps its binding unchanged.

        **Concurrency:** `If-Match` is optional (omitted = last-writer-wins). When
        provided it is compared, under the row lock, against the digest of the latest
        version's manifest; mismatch returns `412` (`etag_mismatch`) carrying the
        current `ETag`. The token is content-addressed, not a version identity: it
        guards "the content I read is still the content in place", so two versions with
        identical manifests are interchangeable for the precondition, and archiving the
        tip does not invalidate a token whose digest the new latest version still
        carries. Do not re-key it on `policy_set_version_id`.

        **Identity and reverts:** a desired state identical to the **latest** version is
        a no-op (`created: false`, latest returned, nothing minted). A desired state
        matching an **older** version mints a new version at the tip — history is
        linear, never forked. Rolling back deployment without a content edit is not an
        apply at all: bind the older version via `PUT /policy-bindings`.

        **Authorization:** the route gate is `update` on the policy set. When
        `activate: true`, the handler additionally requires the `activate` action on
        `policy_set_bindings`.

        Domain error codes: `policy_set_not_found`, `policy_not_found`,
        `policy_version_not_found`, `version_archived`, `schema_version_mismatch`,
        `manifest_duplicate_policy`, `missing_cedar_content`, `invalid_cedar`,
        `schema_version_unsupported`, `policy_name_conflict`, `policy_archived`,
        `set_archived`, `etag_mismatch`, `activate_requires_zone_target`,
        `shadow_equals_active`.

        Args:
          entries: Complete desired content. Order is preserved for newly added policies; retained
              policies keep their current manifest order (so an unchanged apply reproduces the
              identical manifest and dedups).

          dry_run: Not yet implemented — `true` returns 501 until ACC-1002. When true, performs
              validation, schema resolution, and the content diff, and returns the would-be
              `changes` and `warnings` — but persists nothing. `policy_set_version` is omitted
              from the response and no ETag is returned.

          activate: Also rebind the zone/active slot to the resulting version in the same
              transaction. Requires the `activate` permission on policy set bindings. Targets
              only the zone/active slot; other slots go through PUT /policy-bindings.

          schema_version:
              Cedar schema version to validate and pin the resulting version against. Omitted:
              the server resolves it (latest version's schema if still writable, else the zone
              default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/manifest", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=maybe_transform(
                {
                    "entries": entries,
                    "activate": activate,
                    "schema_version": schema_version,
                },
                manifest_apply_params.ManifestApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, manifest_apply_params.ManifestApplyParams),
            ),
            cast_to=ManifestApplyResponse,
        )


class AsyncManifestResource(AsyncAPIResource):
    """Declarative read/apply of a policy set's full content"""

    @cached_property
    def with_raw_response(self) -> AsyncManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncManifestResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestRetrieveResponse:
        """
        Returns the resolved manifest of the **latest non-archived version** by default.
        Pass `?version=` with a policy set version public ID to read a specific
        version's manifest (e.g. for rollback: GET an old manifest, PUT it back — which
        mints a new version at the tip with the old content; history is never
        re-pointed).

        There is deliberately no `?version=active` keyword: a binding slot is
        `(zone, target_type, target_id, mode)` and a set may have zero or several active
        bindings, so "the active version" is not a function of the set alone. Resolve
        the version ID first — from the enriched policy set representation
        (`active_version_id`) or `GET /policy-bindings` — then pass it here.

        The default (latest) read anchors the apply flow: the `ETag` response header is
        the JCS SHA-256 digest of the latest manifest and is the value to send as
        `If-Match` on `PUT`. **`ETag` is emitted only on the default latest read** —
        versioned reads return `manifest_sha` in the body but no `ETag`, so a stale
        token cannot be round-tripped as a precondition.

        A policy set with no versions yet returns `200` with empty `entries`, null
        `policy_set_version_id`/`version`/`schema_version`/`manifest_sha`, and the
        digest of the empty manifest as `ETag`, so even the first apply can be
        conditional.

        Args:
          version: Policy set version public ID. Default: latest non-archived version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/manifest", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, manifest_retrieve_params.ManifestRetrieveParams
                ),
            ),
            cast_to=ManifestRetrieveResponse,
        )

    async def apply(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        entries: Iterable[manifest_apply_params.Entry],
        dry_run: bool | Omit = omit,
        activate: bool | Omit = omit,
        schema_version: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestApplyResponse:
        """Declarative full-replace apply.

        `entries` is the complete desired content of the
        policy set: **any policy omitted from `entries` is dropped from the resulting
        version** (its rows are retained and a later apply may reference it again).
        Entry order is preserved for newly added policies; retained policies keep their
        current manifest order, so an unchanged apply is byte-identical and dedups to
        the existing version.

        Per entry, the server diffs by content SHA against the version pinned in the
        latest manifest: unchanged content under the same schema version reuses the
        pinned policy version; changed content mints a new policy version; `new_policy`
        entries mint a customer-owned policy with the requested name. All of this, plus
        the policy set version mint and the optional activation, happens in **one
        transaction** (row lock on the policy set). Cedar validation runs against the
        resolved schema before the transaction opens — an invalid policy rejects the
        whole apply with zero writes.

        **Schema resolution:** `schema_version` omitted → the latest version's schema if
        still writable, else the zone default. Provided → authoritative
        (`schema_version_unsupported` if unknown, unattested, or archived). All entries
        validate against the single resolved version (uniform-schema-per-version is
        retained); a pinned policy version created under a different schema is
        re-versioned even if its content is unchanged.

        **Activation:** `activate: true` requires a zone-targeted set and rebinds the
        `(zone, target_type=zone, mode=active)` slot to the resulting version in the
        same transaction. It requires `policy_set_bindings:activate` permission and
        preserves the previous binding in binding history. Unchanged content returns
        `created: false` and still activates the resulting version. An already active
        version keeps its binding unchanged.

        **Concurrency:** `If-Match` is optional (omitted = last-writer-wins). When
        provided it is compared, under the row lock, against the digest of the latest
        version's manifest; mismatch returns `412` (`etag_mismatch`) carrying the
        current `ETag`. The token is content-addressed, not a version identity: it
        guards "the content I read is still the content in place", so two versions with
        identical manifests are interchangeable for the precondition, and archiving the
        tip does not invalidate a token whose digest the new latest version still
        carries. Do not re-key it on `policy_set_version_id`.

        **Identity and reverts:** a desired state identical to the **latest** version is
        a no-op (`created: false`, latest returned, nothing minted). A desired state
        matching an **older** version mints a new version at the tip — history is
        linear, never forked. Rolling back deployment without a content edit is not an
        apply at all: bind the older version via `PUT /policy-bindings`.

        **Authorization:** the route gate is `update` on the policy set. When
        `activate: true`, the handler additionally requires the `activate` action on
        `policy_set_bindings`.

        Domain error codes: `policy_set_not_found`, `policy_not_found`,
        `policy_version_not_found`, `version_archived`, `schema_version_mismatch`,
        `manifest_duplicate_policy`, `missing_cedar_content`, `invalid_cedar`,
        `schema_version_unsupported`, `policy_name_conflict`, `policy_archived`,
        `set_archived`, `etag_mismatch`, `activate_requires_zone_target`,
        `shadow_equals_active`.

        Args:
          entries: Complete desired content. Order is preserved for newly added policies; retained
              policies keep their current manifest order (so an unchanged apply reproduces the
              identical manifest and dedups).

          dry_run: Not yet implemented — `true` returns 501 until ACC-1002. When true, performs
              validation, schema resolution, and the content diff, and returns the would-be
              `changes` and `warnings` — but persists nothing. `policy_set_version` is omitted
              from the response and no ETag is returned.

          activate: Also rebind the zone/active slot to the resulting version in the same
              transaction. Requires the `activate` permission on policy set bindings. Targets
              only the zone/active slot; other slots go through PUT /policy-bindings.

          schema_version:
              Cedar schema version to validate and pin the resulting version against. Omitted:
              the server resolves it (latest version's schema if still writable, else the zone
              default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/manifest", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=await async_maybe_transform(
                {
                    "entries": entries,
                    "activate": activate,
                    "schema_version": schema_version,
                },
                manifest_apply_params.ManifestApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, manifest_apply_params.ManifestApplyParams),
            ),
            cast_to=ManifestApplyResponse,
        )


class ManifestResourceWithRawResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = to_raw_response_wrapper(
            manifest.retrieve,
        )
        self.apply = to_raw_response_wrapper(
            manifest.apply,
        )


class AsyncManifestResourceWithRawResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = async_to_raw_response_wrapper(
            manifest.retrieve,
        )
        self.apply = async_to_raw_response_wrapper(
            manifest.apply,
        )


class ManifestResourceWithStreamingResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = to_streamed_response_wrapper(
            manifest.retrieve,
        )
        self.apply = to_streamed_response_wrapper(
            manifest.apply,
        )


class AsyncManifestResourceWithStreamingResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = async_to_streamed_response_wrapper(
            manifest.retrieve,
        )
        self.apply = async_to_streamed_response_wrapper(
            manifest.apply,
        )
