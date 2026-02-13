# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import delegated_grant_list_params, delegated_grant_update_params
from ..._base_client import make_request_options
from ...types.zones.grant import Grant
from ...types.zones.delegated_grant_list_response import DelegatedGrantListResponse

__all__ = ["DelegatedGrantsResource", "AsyncDelegatedGrantsResource"]


class DelegatedGrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DelegatedGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return DelegatedGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DelegatedGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return DelegatedGrantsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """
        Returns details of a specific delegated grant by grant ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/delegated-grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    def update(
        self,
        id: str,
        *,
        zone_id: str,
        status: Literal["revoked"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """
        Revokes an active delegated grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._patch(
            f"/zones/{zone_id}/delegated-grants/{id}",
            body=maybe_transform({"status": status}, delegated_grant_update_params.DelegatedGrantUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    def list(
        self,
        zone_id: str,
        *,
        active: Literal["true"] | Omit = omit,
        resource_id: str | Omit = omit,
        status: Literal["active", "expired", "revoked"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DelegatedGrantListResponse:
        """Returns a list of delegated grants in the specified zone.

        Can be filtered by
        user, resource, or status.

        Args:
          resource_id: Filter by resource ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/delegated-grants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "resource_id": resource_id,
                        "status": status,
                        "user_id": user_id,
                    },
                    delegated_grant_list_params.DelegatedGrantListParams,
                ),
            ),
            cast_to=DelegatedGrantListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently revokes a delegated grant, removing the user's access to the
        protected resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return self._delete(
            f"/zones/{zone_id}/delegated-grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDelegatedGrantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDelegatedGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDelegatedGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDelegatedGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return AsyncDelegatedGrantsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """
        Returns details of a specific delegated grant by grant ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/delegated-grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        status: Literal["revoked"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """
        Revokes an active delegated grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._patch(
            f"/zones/{zone_id}/delegated-grants/{id}",
            body=await async_maybe_transform(
                {"status": status}, delegated_grant_update_params.DelegatedGrantUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    async def list(
        self,
        zone_id: str,
        *,
        active: Literal["true"] | Omit = omit,
        resource_id: str | Omit = omit,
        status: Literal["active", "expired", "revoked"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DelegatedGrantListResponse:
        """Returns a list of delegated grants in the specified zone.

        Can be filtered by
        user, resource, or status.

        Args:
          resource_id: Filter by resource ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/delegated-grants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "resource_id": resource_id,
                        "status": status,
                        "user_id": user_id,
                    },
                    delegated_grant_list_params.DelegatedGrantListParams,
                ),
            ),
            cast_to=DelegatedGrantListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently revokes a delegated grant, removing the user's access to the
        protected resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return await self._delete(
            f"/zones/{zone_id}/delegated-grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DelegatedGrantsResourceWithRawResponse:
    def __init__(self, delegated_grants: DelegatedGrantsResource) -> None:
        self._delegated_grants = delegated_grants

        self.retrieve = to_raw_response_wrapper(
            delegated_grants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            delegated_grants.update,
        )
        self.list = to_raw_response_wrapper(
            delegated_grants.list,
        )
        self.delete = to_raw_response_wrapper(
            delegated_grants.delete,
        )


class AsyncDelegatedGrantsResourceWithRawResponse:
    def __init__(self, delegated_grants: AsyncDelegatedGrantsResource) -> None:
        self._delegated_grants = delegated_grants

        self.retrieve = async_to_raw_response_wrapper(
            delegated_grants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            delegated_grants.update,
        )
        self.list = async_to_raw_response_wrapper(
            delegated_grants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            delegated_grants.delete,
        )


class DelegatedGrantsResourceWithStreamingResponse:
    def __init__(self, delegated_grants: DelegatedGrantsResource) -> None:
        self._delegated_grants = delegated_grants

        self.retrieve = to_streamed_response_wrapper(
            delegated_grants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            delegated_grants.update,
        )
        self.list = to_streamed_response_wrapper(
            delegated_grants.list,
        )
        self.delete = to_streamed_response_wrapper(
            delegated_grants.delete,
        )


class AsyncDelegatedGrantsResourceWithStreamingResponse:
    def __init__(self, delegated_grants: AsyncDelegatedGrantsResource) -> None:
        self._delegated_grants = delegated_grants

        self.retrieve = async_to_streamed_response_wrapper(
            delegated_grants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            delegated_grants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            delegated_grants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            delegated_grants.delete,
        )
