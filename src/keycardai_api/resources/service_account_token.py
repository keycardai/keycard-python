# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import service_account_token_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.token_response import TokenResponse

__all__ = ["ServiceAccountTokenResource", "AsyncServiceAccountTokenResource"]


class ServiceAccountTokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceAccountTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ServiceAccountTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceAccountTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return ServiceAccountTokenResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["client_credentials"],
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Exchange service account credentials for organization-scoped M2M token

        Args:
          client_id: Service account client ID

          client_secret: Service account client secret

          grant_type: OAuth 2.0 grant type (must be "client_credentials")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            "/service-account-token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                },
                service_account_token_create_params.ServiceAccountTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=TokenResponse,
        )


class AsyncServiceAccountTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceAccountTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceAccountTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceAccountTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return AsyncServiceAccountTokenResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["client_credentials"],
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Exchange service account credentials for organization-scoped M2M token

        Args:
          client_id: Service account client ID

          client_secret: Service account client secret

          grant_type: OAuth 2.0 grant type (must be "client_credentials")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            "/service-account-token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                },
                service_account_token_create_params.ServiceAccountTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=TokenResponse,
        )


class ServiceAccountTokenResourceWithRawResponse:
    def __init__(self, service_account_token: ServiceAccountTokenResource) -> None:
        self._service_account_token = service_account_token

        self.create = to_raw_response_wrapper(
            service_account_token.create,
        )


class AsyncServiceAccountTokenResourceWithRawResponse:
    def __init__(self, service_account_token: AsyncServiceAccountTokenResource) -> None:
        self._service_account_token = service_account_token

        self.create = async_to_raw_response_wrapper(
            service_account_token.create,
        )


class ServiceAccountTokenResourceWithStreamingResponse:
    def __init__(self, service_account_token: ServiceAccountTokenResource) -> None:
        self._service_account_token = service_account_token

        self.create = to_streamed_response_wrapper(
            service_account_token.create,
        )


class AsyncServiceAccountTokenResourceWithStreamingResponse:
    def __init__(self, service_account_token: AsyncServiceAccountTokenResource) -> None:
        self._service_account_token = service_account_token

        self.create = async_to_streamed_response_wrapper(
            service_account_token.create,
        )
