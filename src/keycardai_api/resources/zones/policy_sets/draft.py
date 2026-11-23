# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.zones.policy_sets import (
    draft_create_params,
    draft_update_params,
    draft_upsert_params,
    draft_retrieve_params,
    draft_list_policies_params,
)
from ....types.zones.policy_set_draft import PolicySetDraft
from ....types.zones.policy_set_manifest_param import PolicySetManifestParam
from ....types.zones.policy_sets.draft_list_policies_response import DraftListPoliciesResponse

__all__ = ["DraftResource", "AsyncDraftResource"]


class DraftResource(SyncAPIResource):
    """Mutable policy set manifest workspace"""

    @cached_property
    def with_raw_response(self) -> DraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return DraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return DraftResourceWithStreamingResponse(self)

    def create(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        base_version_id: str | Omit = omit,
        description: str | Omit = omit,
        manifest: PolicySetManifestParam | Omit = omit,
        name: str | Omit = omit,
        schema_version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Safe draft creation that never overwrites an existing draft.

        If a draft already
        exists for this policy set, it is returned as-is (200 OK). Three body modes
        control how a new draft is initialized: (1) empty body — hydrate from the latest
        non-archived version, (2) { base_version_id } — hydrate from a specific version,
        (3) full body with manifest and schema_version — create with explicit content.
        base_version_id and manifest are mutually exclusive; providing both is rejected.

        Args:
          base_version_id: ID of a policy set version to hydrate from. Mutually exclusive with manifest —
              the server rejects requests containing both fields.

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
        return self._post(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=maybe_transform(
                {
                    "base_version_id": base_version_id,
                    "description": description,
                    "manifest": manifest,
                    "name": name,
                    "schema_version": schema_version,
                },
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )

    def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["user"], List[Literal["user"]]] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """
        Get the draft for a policy set

        Args:
          expand: Opt-in to additional response fields on a single resource (`user`). Repeatable.

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
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, draft_retrieve_params.DraftRetrieveParams),
            ),
            cast_to=PolicySetDraft,
        )

    def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
        manifest_operations: Iterable[draft_update_params.ManifestOperation] | Omit = omit,
        name: str | Omit = omit,
        schema_version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Applies partial updates to an existing draft.

        Supports updating metadata fields
        (name, description, schema_version) and manifest operations (set, add, remove
        entries).

        Args:
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
        return self._patch(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "manifest_operations": manifest_operations,
                    "name": name,
                    "schema_version": schema_version,
                },
                draft_update_params.DraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )

    def delete(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a policy set draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_policies(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListPoliciesResponse:
        """
        Returns the policy versions referenced by the draft's manifest as a paginated
        list. Mirrors the published
        `/policy-sets/{policy_set_id}/versions/{version_id}/policies` endpoint but
        sources entries from the policy set's mutable draft. Archived policy versions
        referenced by the manifest are still returned.

        Args:
          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: Opt-in to additional response fields (`total_count`, `user`). Repeatable;
              matches the `expand[]` convention used across the Keycard API.

          format: Narrows which Cedar representation the response includes. When omitted, both
              `cedar_json` and `cedar_raw` are populated. Pass `json` to receive only
              `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that don't care
              about payload size can skip this parameter.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          sort: Field to sort by.

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
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft/policies",
                zone_id=zone_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "expand": expand,
                        "format": format,
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    draft_list_policies_params.DraftListPoliciesParams,
                ),
            ),
            cast_to=DraftListPoliciesResponse,
        )

    def upsert(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        manifest: PolicySetManifestParam,
        schema_version: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Full replacement of the draft state.

        Creates the draft if it does not exist,
        replaces it if it does. Standard REST PUT idempotency — the caller provides the
        complete desired state.

        Args:
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
        return self._put(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=maybe_transform(
                {
                    "manifest": manifest,
                    "schema_version": schema_version,
                    "description": description,
                    "name": name,
                },
                draft_upsert_params.DraftUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )


class AsyncDraftResource(AsyncAPIResource):
    """Mutable policy set manifest workspace"""

    @cached_property
    def with_raw_response(self) -> AsyncDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncDraftResourceWithStreamingResponse(self)

    async def create(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        base_version_id: str | Omit = omit,
        description: str | Omit = omit,
        manifest: PolicySetManifestParam | Omit = omit,
        name: str | Omit = omit,
        schema_version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Safe draft creation that never overwrites an existing draft.

        If a draft already
        exists for this policy set, it is returned as-is (200 OK). Three body modes
        control how a new draft is initialized: (1) empty body — hydrate from the latest
        non-archived version, (2) { base_version_id } — hydrate from a specific version,
        (3) full body with manifest and schema_version — create with explicit content.
        base_version_id and manifest are mutually exclusive; providing both is rejected.

        Args:
          base_version_id: ID of a policy set version to hydrate from. Mutually exclusive with manifest —
              the server rejects requests containing both fields.

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
        return await self._post(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=await async_maybe_transform(
                {
                    "base_version_id": base_version_id,
                    "description": description,
                    "manifest": manifest,
                    "name": name,
                    "schema_version": schema_version,
                },
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )

    async def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["user"], List[Literal["user"]]] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """
        Get the draft for a policy set

        Args:
          expand: Opt-in to additional response fields on a single resource (`user`). Repeatable.

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
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, draft_retrieve_params.DraftRetrieveParams),
            ),
            cast_to=PolicySetDraft,
        )

    async def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
        manifest_operations: Iterable[draft_update_params.ManifestOperation] | Omit = omit,
        name: str | Omit = omit,
        schema_version: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Applies partial updates to an existing draft.

        Supports updating metadata fields
        (name, description, schema_version) and manifest operations (set, add, remove
        entries).

        Args:
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
        return await self._patch(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "manifest_operations": manifest_operations,
                    "name": name,
                    "schema_version": schema_version,
                },
                draft_update_params.DraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )

    async def delete(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a policy set draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_policies(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListPoliciesResponse:
        """
        Returns the policy versions referenced by the draft's manifest as a paginated
        list. Mirrors the published
        `/policy-sets/{policy_set_id}/versions/{version_id}/policies` endpoint but
        sources entries from the policy set's mutable draft. Archived policy versions
        referenced by the manifest are still returned.

        Args:
          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: Opt-in to additional response fields (`total_count`, `user`). Repeatable;
              matches the `expand[]` convention used across the Keycard API.

          format: Narrows which Cedar representation the response includes. When omitted, both
              `cedar_json` and `cedar_raw` are populated. Pass `json` to receive only
              `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that don't care
              about payload size can skip this parameter.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          sort: Field to sort by.

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
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft/policies",
                zone_id=zone_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "expand": expand,
                        "format": format,
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    draft_list_policies_params.DraftListPoliciesParams,
                ),
            ),
            cast_to=DraftListPoliciesResponse,
        )

    async def upsert(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        manifest: PolicySetManifestParam,
        schema_version: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDraft:
        """Full replacement of the draft state.

        Creates the draft if it does not exist,
        replaces it if it does. Standard REST PUT idempotency — the caller provides the
        complete desired state.

        Args:
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
        return await self._put(
            path_template(
                "/zones/{zone_id}/policy-sets/{policy_set_id}/draft", zone_id=zone_id, policy_set_id=policy_set_id
            ),
            body=await async_maybe_transform(
                {
                    "manifest": manifest,
                    "schema_version": schema_version,
                    "description": description,
                    "name": name,
                },
                draft_upsert_params.DraftUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetDraft,
        )


class DraftResourceWithRawResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.create = to_raw_response_wrapper(
            draft.create,
        )
        self.retrieve = to_raw_response_wrapper(
            draft.retrieve,
        )
        self.update = to_raw_response_wrapper(
            draft.update,
        )
        self.delete = to_raw_response_wrapper(
            draft.delete,
        )
        self.list_policies = to_raw_response_wrapper(
            draft.list_policies,
        )
        self.upsert = to_raw_response_wrapper(
            draft.upsert,
        )


class AsyncDraftResourceWithRawResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.create = async_to_raw_response_wrapper(
            draft.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            draft.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            draft.update,
        )
        self.delete = async_to_raw_response_wrapper(
            draft.delete,
        )
        self.list_policies = async_to_raw_response_wrapper(
            draft.list_policies,
        )
        self.upsert = async_to_raw_response_wrapper(
            draft.upsert,
        )


class DraftResourceWithStreamingResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.create = to_streamed_response_wrapper(
            draft.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            draft.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            draft.update,
        )
        self.delete = to_streamed_response_wrapper(
            draft.delete,
        )
        self.list_policies = to_streamed_response_wrapper(
            draft.list_policies,
        )
        self.upsert = to_streamed_response_wrapper(
            draft.upsert,
        )


class AsyncDraftResourceWithStreamingResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.create = async_to_streamed_response_wrapper(
            draft.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            draft.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            draft.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            draft.delete,
        )
        self.list_policies = async_to_streamed_response_wrapper(
            draft.list_policies,
        )
        self.upsert = async_to_streamed_response_wrapper(
            draft.upsert,
        )
