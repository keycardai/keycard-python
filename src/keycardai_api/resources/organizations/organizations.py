# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...types import (
    organization_list_params,
    organization_create_params,
    organization_update_params,
    organization_retrieve_params,
)
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
from .invitations import (
    InvitationsResource,
    AsyncInvitationsResource,
    InvitationsResourceWithRawResponse,
    AsyncInvitationsResourceWithRawResponse,
    InvitationsResourceWithStreamingResponse,
    AsyncInvitationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .sso_connection import (
    SSOConnectionResource,
    AsyncSSOConnectionResource,
    SSOConnectionResourceWithRawResponse,
    AsyncSSOConnectionResourceWithRawResponse,
    SSOConnectionResourceWithStreamingResponse,
    AsyncSSOConnectionResourceWithStreamingResponse,
)
from ...types.organization import Organization
from .service_accounts.service_accounts import (
    ServiceAccountsResource,
    AsyncServiceAccountsResource,
    ServiceAccountsResourceWithRawResponse,
    AsyncServiceAccountsResourceWithRawResponse,
    ServiceAccountsResourceWithStreamingResponse,
    AsyncServiceAccountsResourceWithStreamingResponse,
)
from ...types.organization_list_response import OrganizationListResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def invitations(self) -> InvitationsResource:
        return InvitationsResource(self._client)

    @cached_property
    def service_accounts(self) -> ServiceAccountsResource:
        return ServiceAccountsResource(self._client)

    @cached_property
    def sso_connection(self) -> SSOConnectionResource:
        return SSOConnectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Args:
          name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            "/organizations",
            body=maybe_transform({"name": name}, organization_create_params.OrganizationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def retrieve(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions", "total_count"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Get organization by ID or label

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For list
              organization identities only, "total_count" populates pagination.total_count
              with the number of identities matching the same filters as the list (excluding
              cursor and limit). Other operations ignore expand values they do not use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, organization_retrieve_params.OrganizationRetrieveParams),
            ),
            cast_to=Organization,
        )

    def update(
        self,
        organization_id: str,
        *,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Update organization details

        Args:
          organization_id: Organization ID or label identifier

          name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._patch(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            body=maybe_transform({"name": name}, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions", "total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListResponse:
        """
        List organizations for the current user

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For list
              organization identities only, "total_count" populates pagination.total_count
              with the number of identities matching the same filters as the list (excluding
              cursor and limit). Other operations ignore expand values they do not use.

          limit: Maximum number of organizations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            "/organizations",
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
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=OrganizationListResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        return AsyncInvitationsResource(self._client)

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResource:
        return AsyncServiceAccountsResource(self._client)

    @cached_property
    def sso_connection(self) -> AsyncSSOConnectionResource:
        return AsyncSSOConnectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Args:
          name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            "/organizations",
            body=await async_maybe_transform({"name": name}, organization_create_params.OrganizationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    async def retrieve(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions", "total_count"]] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Get organization by ID or label

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For list
              organization identities only, "total_count" populates pagination.total_count
              with the number of identities matching the same filters as the list (excluding
              cursor and limit). Other operations ignore expand values they do not use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, organization_retrieve_params.OrganizationRetrieveParams
                ),
            ),
            cast_to=Organization,
        )

    async def update(
        self,
        organization_id: str,
        *,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Update organization details

        Args:
          organization_id: Organization ID or label identifier

          name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._patch(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            body=await async_maybe_transform({"name": name}, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions", "total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListResponse:
        """
        List organizations for the current user

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For list
              organization identities only, "total_count" populates pagination.total_count
              with the number of identities matching the same filters as the list (excluding
              cursor and limit). Other operations ignore expand values they do not use.

          limit: Maximum number of organizations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            "/organizations",
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
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=OrganizationListResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )

    @cached_property
    def invitations(self) -> InvitationsResourceWithRawResponse:
        return InvitationsResourceWithRawResponse(self._organizations.invitations)

    @cached_property
    def service_accounts(self) -> ServiceAccountsResourceWithRawResponse:
        return ServiceAccountsResourceWithRawResponse(self._organizations.service_accounts)

    @cached_property
    def sso_connection(self) -> SSOConnectionResourceWithRawResponse:
        return SSOConnectionResourceWithRawResponse(self._organizations.sso_connection)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithRawResponse:
        return AsyncInvitationsResourceWithRawResponse(self._organizations.invitations)

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResourceWithRawResponse:
        return AsyncServiceAccountsResourceWithRawResponse(self._organizations.service_accounts)

    @cached_property
    def sso_connection(self) -> AsyncSSOConnectionResourceWithRawResponse:
        return AsyncSSOConnectionResourceWithRawResponse(self._organizations.sso_connection)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )

    @cached_property
    def invitations(self) -> InvitationsResourceWithStreamingResponse:
        return InvitationsResourceWithStreamingResponse(self._organizations.invitations)

    @cached_property
    def service_accounts(self) -> ServiceAccountsResourceWithStreamingResponse:
        return ServiceAccountsResourceWithStreamingResponse(self._organizations.service_accounts)

    @cached_property
    def sso_connection(self) -> SSOConnectionResourceWithStreamingResponse:
        return SSOConnectionResourceWithStreamingResponse(self._organizations.sso_connection)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithStreamingResponse:
        return AsyncInvitationsResourceWithStreamingResponse(self._organizations.invitations)

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        return AsyncServiceAccountsResourceWithStreamingResponse(self._organizations.service_accounts)

    @cached_property
    def sso_connection(self) -> AsyncSSOConnectionResourceWithStreamingResponse:
        return AsyncSSOConnectionResourceWithStreamingResponse(self._organizations.sso_connection)
