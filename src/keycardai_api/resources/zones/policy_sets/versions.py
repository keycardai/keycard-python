# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
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
    version_list_params,
    version_create_params,
    version_update_params,
    version_list_policies_params,
)
from ....types.zones.policy_set_manifest_param import PolicySetManifestParam
from ....types.zones.policy_sets.policy_set_version import PolicySetVersion
from ....types.zones.policy_sets.version_list_response import VersionListResponse
from ....types.zones.policy_sets.version_list_policies_response import VersionListPoliciesResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    """Immutable policy set manifest snapshots"""

    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        manifest: PolicySetManifestParam,
        schema_version: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Validates the manifest, computes SHA, and creates an immutable version snapshot.

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
        return self._post(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions",
            body=maybe_transform(
                {
                    "manifest": manifest,
                    "schema_version": schema_version,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    def retrieve(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Get a specific policy set version

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    def update(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        active: Literal[True],
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Set active=true to bind this version as the active zone policy set.

        Args:
          active: Must be true. Binds this version as the active zone policy set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            body=maybe_transform({"active": active}, version_update_params.VersionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    def list(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
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
    ) -> VersionListResponse:
        """
        List versions of a policy set

        Args:
          after: Return items after this cursor (forward pagination). Use after_cursor from a
              previous response. Mutually exclusive with before.

          before: Return items before this cursor (backward pagination). Use before_cursor from a
              previous response. Mutually exclusive with after.

          expand: Opt-in to additional response fields

          limit: Maximum number of items to return

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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions",
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
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            cast_to=VersionListResponse,
        )

    def archive(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Archive a policy set version

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    def list_policies(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
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
    ) -> VersionListPoliciesResponse:
        """
        Returns the policy versions referenced by this policy set version's manifest as
        a paginated list.

        Args:
          after: Return items after this cursor (forward pagination). Use after_cursor from a
              previous response. Mutually exclusive with before.

          before: Return items before this cursor (backward pagination). Use before_cursor from a
              previous response. Mutually exclusive with after.

          expand: Opt-in to additional response fields

          format: Policy representation format. `json` returns cedar_json, `cedar` returns
              cedar_raw.

          limit: Maximum number of items to return

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}/policies",
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
                    version_list_policies_params.VersionListPoliciesParams,
                ),
            ),
            cast_to=VersionListPoliciesResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    """Immutable policy set manifest snapshots"""

    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        manifest: PolicySetManifestParam,
        schema_version: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Validates the manifest, computes SHA, and creates an immutable version snapshot.

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
        return await self._post(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions",
            body=await async_maybe_transform(
                {
                    "manifest": manifest,
                    "schema_version": schema_version,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    async def retrieve(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Get a specific policy set version

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    async def update(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        active: Literal[True],
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Set active=true to bind this version as the active zone policy set.

        Args:
          active: Must be true. Binds this version as the active zone policy set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            body=await async_maybe_transform({"active": active}, version_update_params.VersionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    async def list(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
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
    ) -> VersionListResponse:
        """
        List versions of a policy set

        Args:
          after: Return items after this cursor (forward pagination). Use after_cursor from a
              previous response. Mutually exclusive with before.

          before: Return items before this cursor (backward pagination). Use before_cursor from a
              previous response. Mutually exclusive with after.

          expand: Opt-in to additional response fields

          limit: Maximum number of items to return

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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions",
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
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            cast_to=VersionListResponse,
        )

    async def archive(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetVersion:
        """
        Archive a policy set version

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetVersion,
        )

    async def list_policies(
        self,
        version_id: str,
        *,
        zone_id: str,
        policy_set_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
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
    ) -> VersionListPoliciesResponse:
        """
        Returns the policy versions referenced by this policy set version's manifest as
        a paginated list.

        Args:
          after: Return items after this cursor (forward pagination). Use after_cursor from a
              previous response. Mutually exclusive with before.

          before: Return items before this cursor (backward pagination). Use before_cursor from a
              previous response. Mutually exclusive with after.

          expand: Opt-in to additional response fields

          format: Policy representation format. `json` returns cedar_json, `cedar` returns
              cedar_raw.

          limit: Maximum number of items to return

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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
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
            f"/zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}/policies",
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
                    version_list_policies_params.VersionListPoliciesParams,
                ),
            ),
            cast_to=VersionListPoliciesResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            versions.update,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.archive = to_raw_response_wrapper(
            versions.archive,
        )
        self.list_policies = to_raw_response_wrapper(
            versions.list_policies,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            versions.update,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.archive = async_to_raw_response_wrapper(
            versions.archive,
        )
        self.list_policies = async_to_raw_response_wrapper(
            versions.list_policies,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            versions.update,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.archive = to_streamed_response_wrapper(
            versions.archive,
        )
        self.list_policies = to_streamed_response_wrapper(
            versions.list_policies,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            versions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            versions.archive,
        )
        self.list_policies = async_to_streamed_response_wrapper(
            versions.list_policies,
        )
