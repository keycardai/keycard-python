# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
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
from ....types.zones import policy_set_list_params, policy_set_create_params, policy_set_update_params
from ...._base_client import make_request_options
from ....types.zones.policy_set_with_binding import PolicySetWithBinding
from ....types.zones.policy_set_list_response import PolicySetListResponse

__all__ = ["PolicySetsResource", "AsyncPolicySetsResource"]


class PolicySetsResource(SyncAPIResource):
    """Policy set CRUD and binding management"""

    @cached_property
    def versions(self) -> VersionsResource:
        """Immutable policy set manifest snapshots"""
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicySetsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        name: str,
        scope_type: Literal["zone", "resource", "user", "session"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Creates an unbound policy set.

        Use updatePolicySet to bind after creating a
        version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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
            f"/zones/{zone_id}/policy-sets",
            body=maybe_transform(
                {
                    "name": name,
                    "scope_type": scope_type,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    def retrieve(
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
    ) -> PolicySetWithBinding:
        """
        Returns the policy set with current binding information.

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
        return self._get(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        name: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Update metadata or manage binding.

        Set active=true to bind, active=false to
        unbind.

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
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            body=maybe_transform({"name": name}, policy_set_update_params.PolicySetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    def list(
        self,
        zone_id: str,
        *,
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
    ) -> PolicySetListResponse:
        """
        List policy sets in a zone

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
            f"/zones/{zone_id}/policy-sets",
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
                    policy_set_list_params.PolicySetListParams,
                ),
                security={},
            ),
            cast_to=PolicySetListResponse,
        )

    def archive(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Archive a policy set

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
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )


class AsyncPolicySetsResource(AsyncAPIResource):
    """Policy set CRUD and binding management"""

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicySetsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        name: str,
        scope_type: Literal["zone", "resource", "user", "session"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Creates an unbound policy set.

        Use updatePolicySet to bind after creating a
        version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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
            f"/zones/{zone_id}/policy-sets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scope_type": scope_type,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    async def retrieve(
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
    ) -> PolicySetWithBinding:
        """
        Returns the policy set with current binding information.

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
        return await self._get(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    async def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        name: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Update metadata or manage binding.

        Set active=true to bind, active=false to
        unbind.

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
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            body=await async_maybe_transform({"name": name}, policy_set_update_params.PolicySetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )

    async def list(
        self,
        zone_id: str,
        *,
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
    ) -> PolicySetListResponse:
        """
        List policy sets in a zone

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
            f"/zones/{zone_id}/policy-sets",
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
                    policy_set_list_params.PolicySetListParams,
                ),
                security={},
            ),
            cast_to=PolicySetListResponse,
        )

    async def archive(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Archive a policy set

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
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/zones/{zone_id}/policy-sets/{policy_set_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=PolicySetWithBinding,
        )


class PolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_raw_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = to_raw_response_wrapper(
            policy_sets.list,
        )
        self.archive = to_raw_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Immutable policy set manifest snapshots"""
        return VersionsResourceWithRawResponse(self._policy_sets.versions)


class AsyncPolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_raw_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_raw_response_wrapper(
            policy_sets.list,
        )
        self.archive = async_to_raw_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResourceWithRawResponse(self._policy_sets.versions)


class PolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.archive = to_streamed_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Immutable policy set manifest snapshots"""
        return VersionsResourceWithStreamingResponse(self._policy_sets.versions)


class AsyncPolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResourceWithStreamingResponse(self._policy_sets.versions)
