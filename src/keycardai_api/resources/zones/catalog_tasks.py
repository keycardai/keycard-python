# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.zones.task import Task

__all__ = ["CatalogTasksResource", "AsyncCatalogTasksResource"]


class CatalogTasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatalogTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return CatalogTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatalogTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return CatalogTasksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        task_id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Returns 200 with task details when pending, running, or failed.

        Returns 303
        redirect to the install when completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/catalog_tasks/{task_id}", zone_id=zone_id, task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )


class AsyncCatalogTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatalogTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCatalogTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatalogTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncCatalogTasksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        task_id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Returns 200 with task details when pending, running, or failed.

        Returns 303
        redirect to the install when completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/catalog_tasks/{task_id}", zone_id=zone_id, task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )


class CatalogTasksResourceWithRawResponse:
    def __init__(self, catalog_tasks: CatalogTasksResource) -> None:
        self._catalog_tasks = catalog_tasks

        self.retrieve = to_raw_response_wrapper(
            catalog_tasks.retrieve,
        )


class AsyncCatalogTasksResourceWithRawResponse:
    def __init__(self, catalog_tasks: AsyncCatalogTasksResource) -> None:
        self._catalog_tasks = catalog_tasks

        self.retrieve = async_to_raw_response_wrapper(
            catalog_tasks.retrieve,
        )


class CatalogTasksResourceWithStreamingResponse:
    def __init__(self, catalog_tasks: CatalogTasksResource) -> None:
        self._catalog_tasks = catalog_tasks

        self.retrieve = to_streamed_response_wrapper(
            catalog_tasks.retrieve,
        )


class AsyncCatalogTasksResourceWithStreamingResponse:
    def __init__(self, catalog_tasks: AsyncCatalogTasksResource) -> None:
        self._catalog_tasks = catalog_tasks

        self.retrieve = async_to_streamed_response_wrapper(
            catalog_tasks.retrieve,
        )
