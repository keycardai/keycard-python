# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import (
    organization_list_params,
    organization_create_params,
    organization_update_params,
    organization_retrieve_params,
    organization_list_roles_params,
    organization_list_identities_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from .service_accounts.service_accounts import (
    ServiceAccountsResource,
    AsyncServiceAccountsResource,
    ServiceAccountsResourceWithRawResponse,
    AsyncServiceAccountsResourceWithRawResponse,
    ServiceAccountsResourceWithStreamingResponse,
    AsyncServiceAccountsResourceWithStreamingResponse,
)
from ...types.organization_list_response import OrganizationListResponse
from ...types.organization_create_response import OrganizationCreateResponse
from ...types.organization_update_response import OrganizationUpdateResponse
from ...types.organization_retrieve_response import OrganizationRetrieveResponse
from ...types.organization_list_roles_response import OrganizationListRolesResponse
from ...types.organization_exchange_token_response import OrganizationExchangeTokenResponse
from ...types.organization_list_identities_response import OrganizationListIdentitiesResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

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

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
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
    ) -> OrganizationCreateResponse:
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
            cast_to=OrganizationCreateResponse,
        )

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
    ) -> OrganizationRetrieveResponse:
        """
        Get organization by ID or label

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
            f"/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, organization_retrieve_params.OrganizationRetrieveParams),
            ),
            cast_to=OrganizationRetrieveResponse,
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
    ) -> OrganizationUpdateResponse:
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
            f"/organizations/{organization_id}",
            body=maybe_transform({"name": name}, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateResponse,
        )

    def list(
        self,
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
    ) -> OrganizationListResponse:
        """
        List organizations for the current user

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

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

    def exchange_token(
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
    ) -> OrganizationExchangeTokenResponse:
        """
        Exchange user token for organization-scoped M2M token

        Args:
          organization_id: Organization ID or label identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            f"/organizations/{organization_id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExchangeTokenResponse,
        )

    def list_identities(
        self,
        organization_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions"]] | Omit = omit,
        limit: int | Omit = omit,
        role: Literal["org_admin", "org_member", "org_viewer"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListIdentitiesResponse:
        """
        List unified view of users and invitations in an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of identities to return

          role: Filter identities by role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            f"/organizations/{organization_id}/identities",
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
                        "role": role,
                    },
                    organization_list_identities_params.OrganizationListIdentitiesParams,
                ),
            ),
            cast_to=OrganizationListIdentitiesResponse,
        )

    def list_roles(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions"]] | Omit = omit,
        scope: Literal["organization", "zone"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListRolesResponse:
        """Returns the list of available roles in the system for the organization.

        This
        includes both organization-level roles (e.g., org_admin, org_member) and
        zone-level roles (e.g., zone_manager, zone_viewer).

        Each role includes:

        - `name`: Internal identifier (e.g., org_admin, zone_manager)
        - `label`: Human-readable display name (e.g., Organization Administrator)
        - `scope`: Whether the role applies at organization or zone level

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          scope: Filter roles by scope (organization or zone level)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            f"/organizations/{organization_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "scope": scope,
                    },
                    organization_list_roles_params.OrganizationListRolesParams,
                ),
            ),
            cast_to=OrganizationListRolesResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

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

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
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
    ) -> OrganizationCreateResponse:
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
            cast_to=OrganizationCreateResponse,
        )

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
    ) -> OrganizationRetrieveResponse:
        """
        Get organization by ID or label

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
            f"/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, organization_retrieve_params.OrganizationRetrieveParams
                ),
            ),
            cast_to=OrganizationRetrieveResponse,
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
    ) -> OrganizationUpdateResponse:
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
            f"/organizations/{organization_id}",
            body=await async_maybe_transform({"name": name}, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateResponse,
        )

    async def list(
        self,
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
    ) -> OrganizationListResponse:
        """
        List organizations for the current user

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

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

    async def exchange_token(
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
    ) -> OrganizationExchangeTokenResponse:
        """
        Exchange user token for organization-scoped M2M token

        Args:
          organization_id: Organization ID or label identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            f"/organizations/{organization_id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExchangeTokenResponse,
        )

    async def list_identities(
        self,
        organization_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["permissions"]] | Omit = omit,
        limit: int | Omit = omit,
        role: Literal["org_admin", "org_member", "org_viewer"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListIdentitiesResponse:
        """
        List unified view of users and invitations in an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of identities to return

          role: Filter identities by role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            f"/organizations/{organization_id}/identities",
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
                        "role": role,
                    },
                    organization_list_identities_params.OrganizationListIdentitiesParams,
                ),
            ),
            cast_to=OrganizationListIdentitiesResponse,
        )

    async def list_roles(
        self,
        organization_id: str,
        *,
        expand: List[Literal["permissions"]] | Omit = omit,
        scope: Literal["organization", "zone"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListRolesResponse:
        """Returns the list of available roles in the system for the organization.

        This
        includes both organization-level roles (e.g., org_admin, org_member) and
        zone-level roles (e.g., zone_manager, zone_viewer).

        Each role includes:

        - `name`: Internal identifier (e.g., org_admin, zone_manager)
        - `label`: Human-readable display name (e.g., Organization Administrator)
        - `scope`: Whether the role applies at organization or zone level

        Args:
          organization_id: Organization ID or label identifier

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          scope: Filter roles by scope (organization or zone level)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            f"/organizations/{organization_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "scope": scope,
                    },
                    organization_list_roles_params.OrganizationListRolesParams,
                ),
            ),
            cast_to=OrganizationListRolesResponse,
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
        self.exchange_token = to_raw_response_wrapper(
            organizations.exchange_token,
        )
        self.list_identities = to_raw_response_wrapper(
            organizations.list_identities,
        )
        self.list_roles = to_raw_response_wrapper(
            organizations.list_roles,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._organizations.users)

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
        self.exchange_token = async_to_raw_response_wrapper(
            organizations.exchange_token,
        )
        self.list_identities = async_to_raw_response_wrapper(
            organizations.list_identities,
        )
        self.list_roles = async_to_raw_response_wrapper(
            organizations.list_roles,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._organizations.users)

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
        self.exchange_token = to_streamed_response_wrapper(
            organizations.exchange_token,
        )
        self.list_identities = to_streamed_response_wrapper(
            organizations.list_identities,
        )
        self.list_roles = to_streamed_response_wrapper(
            organizations.list_roles,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._organizations.users)

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
        self.exchange_token = async_to_streamed_response_wrapper(
            organizations.exchange_token,
        )
        self.list_identities = async_to_streamed_response_wrapper(
            organizations.list_identities,
        )
        self.list_roles = async_to_streamed_response_wrapper(
            organizations.list_roles,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._organizations.users)

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithStreamingResponse:
        return AsyncInvitationsResourceWithStreamingResponse(self._organizations.invitations)

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        return AsyncServiceAccountsResourceWithStreamingResponse(self._organizations.service_accounts)

    @cached_property
    def sso_connection(self) -> AsyncSSOConnectionResourceWithStreamingResponse:
        return AsyncSSOConnectionResourceWithStreamingResponse(self._organizations.sso_connection)
