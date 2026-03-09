# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.organizations import (
    service_account_list_params,
    service_account_create_params,
    service_account_update_params,
    service_account_retrieve_params,
)
from ....types.organizations.service_account import ServiceAccount
from ....types.organizations.service_account_list_response import ServiceAccountListResponse

__all__ = ["ServiceAccountsResource", "AsyncServiceAccountsResource"]


class ServiceAccountsResource(SyncAPIResource):
    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return ServiceAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Create a new service account for an organization

        Args:
          organization_id: Organization ID or label identifier

          name: Service account name

          description: Optional description of the service account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            f"/organizations/{organization_id}/service-accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ServiceAccount,
        )

    def retrieve(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        expand: List[Literal["permissions"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Get a specific service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, service_account_retrieve_params.ServiceAccountRetrieveParams),
                security={},
            ),
            cast_to=ServiceAccount,
        )

    def update(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Update a service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          description: Optional description of the service account

          name: Service account name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._patch(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                service_account_update_params.ServiceAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ServiceAccount,
        )

    def list(
        self,
        organization_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions"]] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountListResponse:
        """
        List service accounts for an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of service accounts to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            f"/organizations/{organization_id}/service-accounts",
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
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
                security={},
            ),
            cast_to=ServiceAccountListResponse,
        )

    def delete(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._delete(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )


class AsyncServiceAccountsResource(AsyncAPIResource):
    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncServiceAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Create a new service account for an organization

        Args:
          organization_id: Organization ID or label identifier

          name: Service account name

          description: Optional description of the service account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            f"/organizations/{organization_id}/service-accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ServiceAccount,
        )

    async def retrieve(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        expand: List[Literal["permissions"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Get a specific service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, service_account_retrieve_params.ServiceAccountRetrieveParams
                ),
                security={},
            ),
            cast_to=ServiceAccount,
        )

    async def update(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """
        Update a service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          description: Optional description of the service account

          name: Service account name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._patch(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                service_account_update_params.ServiceAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ServiceAccount,
        )

    async def list(
        self,
        organization_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions"]] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountListResponse:
        """
        List service accounts for an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of service accounts to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            f"/organizations/{organization_id}/service-accounts",
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
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
                security={},
            ),
            cast_to=ServiceAccountListResponse,
        )

    async def delete(
        self,
        service_account_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a service account

        Args:
          organization_id: Organization ID or label identifier

          service_account_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._delete(
            f"/organizations/{organization_id}/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )


class ServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_raw_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            service_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            service_accounts.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._service_accounts.credentials)


class AsyncServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_raw_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            service_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_accounts.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._service_accounts.credentials)


class ServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            service_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_accounts.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._service_accounts.credentials)


class AsyncServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            service_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_accounts.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._service_accounts.credentials)
