# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zones.applications import dependency_add_params, dependency_list_params
from ....types.zones.applications.resource import Resource
from ....types.zones.applications.dependency_list_response import DependencyListResponse

__all__ = ["DependenciesResource", "AsyncDependenciesResource"]


class DependenciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DependenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return DependenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return DependenciesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Retrieves a specific resource dependency of an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    def list(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        when_accessing: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DependencyListResponse:
        """
        Returns resource dependencies for an application

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
            f"/zones/{zone_id}/applications/{id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "when_accessing": when_accessing,
                    },
                    dependency_list_params.DependencyListParams,
                ),
            ),
            cast_to=DependencyListResponse,
        )

    def add(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        when_accessing: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Adds a resource dependency to an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return self._put(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"when_accessing": when_accessing}, dependency_add_params.DependencyAddParams),
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a resource dependency from an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return self._delete(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDependenciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDependenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return AsyncDependenciesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Retrieves a specific resource dependency of an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    async def list(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        when_accessing: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DependencyListResponse:
        """
        Returns resource dependencies for an application

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
            f"/zones/{zone_id}/applications/{id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "when_accessing": when_accessing,
                    },
                    dependency_list_params.DependencyListParams,
                ),
            ),
            cast_to=DependencyListResponse,
        )

    async def add(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        when_accessing: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Adds a resource dependency to an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return await self._put(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"when_accessing": when_accessing}, dependency_add_params.DependencyAddParams
                ),
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        dependency_id: str,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a resource dependency from an application

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
        if not dependency_id:
            raise ValueError(f"Expected a non-empty value for `dependency_id` but received {dependency_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Authorization": omit})
        return await self._delete(
            f"/zones/{zone_id}/applications/{id}/dependencies/{dependency_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DependenciesResourceWithRawResponse:
    def __init__(self, dependencies: DependenciesResource) -> None:
        self._dependencies = dependencies

        self.retrieve = to_raw_response_wrapper(
            dependencies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            dependencies.list,
        )
        self.add = to_raw_response_wrapper(
            dependencies.add,
        )
        self.remove = to_raw_response_wrapper(
            dependencies.remove,
        )


class AsyncDependenciesResourceWithRawResponse:
    def __init__(self, dependencies: AsyncDependenciesResource) -> None:
        self._dependencies = dependencies

        self.retrieve = async_to_raw_response_wrapper(
            dependencies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            dependencies.list,
        )
        self.add = async_to_raw_response_wrapper(
            dependencies.add,
        )
        self.remove = async_to_raw_response_wrapper(
            dependencies.remove,
        )


class DependenciesResourceWithStreamingResponse:
    def __init__(self, dependencies: DependenciesResource) -> None:
        self._dependencies = dependencies

        self.retrieve = to_streamed_response_wrapper(
            dependencies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            dependencies.list,
        )
        self.add = to_streamed_response_wrapper(
            dependencies.add,
        )
        self.remove = to_streamed_response_wrapper(
            dependencies.remove,
        )


class AsyncDependenciesResourceWithStreamingResponse:
    def __init__(self, dependencies: AsyncDependenciesResource) -> None:
        self._dependencies = dependencies

        self.retrieve = async_to_streamed_response_wrapper(
            dependencies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            dependencies.list,
        )
        self.add = async_to_streamed_response_wrapper(
            dependencies.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            dependencies.remove,
        )
