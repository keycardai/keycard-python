# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import install_list_params, install_create_params
from ..._base_client import make_request_options
from ...types.zones.task import Task
from ...types.zones.install import Install
from ...types.zones.install_list import InstallList

__all__ = ["InstallsResource", "AsyncInstallsResource"]


class InstallsResource(SyncAPIResource):
    """Install packages and manage package installations."""

    @cached_property
    def with_raw_response(self) -> InstallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return InstallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return InstallsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        package_id: str,
        inputs: Dict[str, object] | Omit = omit,
        version: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Create an install of a package

        Args:
          package_id: Public ID of the package to install.

          inputs: Parametric inputs required by the package.

          version: Specific package version to install. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs", zone_id=zone_id),
            body=maybe_transform(
                {
                    "package_id": package_id,
                    "inputs": inputs,
                    "version": version,
                },
                install_create_params.InstallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )

    def retrieve(
        self,
        install_id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Install:
        """
        Get a specific zone install

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not install_id:
            raise ValueError(f"Expected a non-empty value for `install_id` but received {install_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs/{install_id}", zone_id=zone_id, install_id=install_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Install,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallList:
        """List installs in a zone

        Args:
          after: Cursor for forward pagination.

        Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          limit: Maximum number of items to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    install_list_params.InstallListParams,
                ),
                security={},
            ),
            cast_to=InstallList,
        )

    def delete(
        self,
        install_id: str,
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
        """
        Delete a zone install

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not install_id:
            raise ValueError(f"Expected a non-empty value for `install_id` but received {install_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._delete(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs/{install_id}", zone_id=zone_id, install_id=install_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )


class AsyncInstallsResource(AsyncAPIResource):
    """Install packages and manage package installations."""

    @cached_property
    def with_raw_response(self) -> AsyncInstallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncInstallsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        package_id: str,
        inputs: Dict[str, object] | Omit = omit,
        version: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Create an install of a package

        Args:
          package_id: Public ID of the package to install.

          inputs: Parametric inputs required by the package.

          version: Specific package version to install. Defaults to latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "package_id": package_id,
                    "inputs": inputs,
                    "version": version,
                },
                install_create_params.InstallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )

    async def retrieve(
        self,
        install_id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Install:
        """
        Get a specific zone install

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not install_id:
            raise ValueError(f"Expected a non-empty value for `install_id` but received {install_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs/{install_id}", zone_id=zone_id, install_id=install_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Install,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallList:
        """List installs in a zone

        Args:
          after: Cursor for forward pagination.

        Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          limit: Maximum number of items to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    install_list_params.InstallListParams,
                ),
                security={},
            ),
            cast_to=InstallList,
        )

    async def delete(
        self,
        install_id: str,
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
        """
        Delete a zone install

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not install_id:
            raise ValueError(f"Expected a non-empty value for `install_id` but received {install_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._delete(
            ("/" if not self._client._base_url_overridden else "")
            + path_template("/zones/{zone_id}/installs/{install_id}", zone_id=zone_id, install_id=install_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Task,
        )


class InstallsResourceWithRawResponse:
    def __init__(self, installs: InstallsResource) -> None:
        self._installs = installs

        self.create = to_raw_response_wrapper(
            installs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            installs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            installs.list,
        )
        self.delete = to_raw_response_wrapper(
            installs.delete,
        )


class AsyncInstallsResourceWithRawResponse:
    def __init__(self, installs: AsyncInstallsResource) -> None:
        self._installs = installs

        self.create = async_to_raw_response_wrapper(
            installs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            installs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            installs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            installs.delete,
        )


class InstallsResourceWithStreamingResponse:
    def __init__(self, installs: InstallsResource) -> None:
        self._installs = installs

        self.create = to_streamed_response_wrapper(
            installs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            installs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            installs.list,
        )
        self.delete = to_streamed_response_wrapper(
            installs.delete,
        )


class AsyncInstallsResourceWithStreamingResponse:
    def __init__(self, installs: AsyncInstallsResource) -> None:
        self._installs = installs

        self.create = async_to_streamed_response_wrapper(
            installs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            installs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            installs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            installs.delete,
        )
