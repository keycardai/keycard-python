# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations import (
    sso_connection_enable_params,
    sso_connection_update_params,
    sso_connection_retrieve_params,
)
from ...types.organizations.sso_connection import SSOConnection
from ...types.organizations.sso_connection_protocol_param import SSOConnectionProtocolParam

__all__ = ["SSOConnectionResource", "AsyncSSOConnectionResource"]


class SSOConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSOConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return SSOConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSOConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return SSOConnectionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Get SSO connection configuration for organization

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, sso_connection_retrieve_params.SSOConnectionRetrieveParams),
            ),
            cast_to=SSOConnection,
        )

    def update(
        self,
        organization_id: str,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        identifier: str | Omit = omit,
        protocols: Optional[SSOConnectionProtocolParam] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Update SSO connection configuration

        Args:
          organization_id: Organization ID or label identifier

          client_id: OAuth 2.0 client ID (set to null to remove)

          client_secret: OAuth 2.0 client secret (set to null to remove)

          identifier: SSO provider identifier (e.g., issuer URL)

          protocols: Protocol configuration for SSO connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._patch(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "identifier": identifier,
                    "protocols": protocols,
                },
                sso_connection_update_params.SSOConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConnection,
        )

    def disable(
        self,
        organization_id: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disable SSO for organization

        Args:
          organization_id: Organization ID or label identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def enable(
        self,
        organization_id: str,
        *,
        client_id: str,
        identifier: str,
        client_secret: str | Omit = omit,
        protocols: Optional[SSOConnectionProtocolParam] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Enable SSO for organization

        Args:
          organization_id: Organization ID or label identifier

          client_id: OAuth 2.0 client ID

          identifier: SSO provider identifier (e.g., issuer URL)

          client_secret: OAuth 2.0 client secret (optional, will be encrypted if provided)

          protocols: Protocol configuration for SSO connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "identifier": identifier,
                    "client_secret": client_secret,
                    "protocols": protocols,
                },
                sso_connection_enable_params.SSOConnectionEnableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConnection,
        )


class AsyncSSOConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSOConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSOConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSOConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncSSOConnectionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Get SSO connection configuration for organization

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, sso_connection_retrieve_params.SSOConnectionRetrieveParams
                ),
            ),
            cast_to=SSOConnection,
        )

    async def update(
        self,
        organization_id: str,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        identifier: str | Omit = omit,
        protocols: Optional[SSOConnectionProtocolParam] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Update SSO connection configuration

        Args:
          organization_id: Organization ID or label identifier

          client_id: OAuth 2.0 client ID (set to null to remove)

          client_secret: OAuth 2.0 client secret (set to null to remove)

          identifier: SSO provider identifier (e.g., issuer URL)

          protocols: Protocol configuration for SSO connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._patch(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "identifier": identifier,
                    "protocols": protocols,
                },
                sso_connection_update_params.SSOConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConnection,
        )

    async def disable(
        self,
        organization_id: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disable SSO for organization

        Args:
          organization_id: Organization ID or label identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def enable(
        self,
        organization_id: str,
        *,
        client_id: str,
        identifier: str,
        client_secret: str | Omit = omit,
        protocols: Optional[SSOConnectionProtocolParam] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOConnection:
        """
        Enable SSO for organization

        Args:
          organization_id: Organization ID or label identifier

          client_id: OAuth 2.0 client ID

          identifier: SSO provider identifier (e.g., issuer URL)

          client_secret: OAuth 2.0 client secret (optional, will be encrypted if provided)

          protocols: Protocol configuration for SSO connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/organizations/{organization_id}/sso-connection", organization_id=organization_id),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "identifier": identifier,
                    "client_secret": client_secret,
                    "protocols": protocols,
                },
                sso_connection_enable_params.SSOConnectionEnableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConnection,
        )


class SSOConnectionResourceWithRawResponse:
    def __init__(self, sso_connection: SSOConnectionResource) -> None:
        self._sso_connection = sso_connection

        self.retrieve = to_raw_response_wrapper(
            sso_connection.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sso_connection.update,
        )
        self.disable = to_raw_response_wrapper(
            sso_connection.disable,
        )
        self.enable = to_raw_response_wrapper(
            sso_connection.enable,
        )


class AsyncSSOConnectionResourceWithRawResponse:
    def __init__(self, sso_connection: AsyncSSOConnectionResource) -> None:
        self._sso_connection = sso_connection

        self.retrieve = async_to_raw_response_wrapper(
            sso_connection.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sso_connection.update,
        )
        self.disable = async_to_raw_response_wrapper(
            sso_connection.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            sso_connection.enable,
        )


class SSOConnectionResourceWithStreamingResponse:
    def __init__(self, sso_connection: SSOConnectionResource) -> None:
        self._sso_connection = sso_connection

        self.retrieve = to_streamed_response_wrapper(
            sso_connection.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sso_connection.update,
        )
        self.disable = to_streamed_response_wrapper(
            sso_connection.disable,
        )
        self.enable = to_streamed_response_wrapper(
            sso_connection.enable,
        )


class AsyncSSOConnectionResourceWithStreamingResponse:
    def __init__(self, sso_connection: AsyncSSOConnectionResource) -> None:
        self._sso_connection = sso_connection

        self.retrieve = async_to_streamed_response_wrapper(
            sso_connection.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sso_connection.update,
        )
        self.disable = async_to_streamed_response_wrapper(
            sso_connection.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            sso_connection.enable,
        )
