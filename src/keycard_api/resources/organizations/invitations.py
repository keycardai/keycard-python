# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations import OrganizationRole, invitation_list_params, invitation_create_params
from ...types.organizations.invitation import Invitation
from ...types.organizations.organization_role import OrganizationRole
from ...types.organizations.invitation_list_response import InvitationListResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrganizationRole | Omit = omit,
        x_client_request_id: str | Omit = omit,
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """
        Create an invitation to join an organization

        Args:
          organization_id: Organization ID or label identifier

          email: Email address to invite

          role: Role to assign when invitation is accepted (defaults to org_admin if not
              provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._post(
            f"/organizations/{organization_id}/invitations",
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invitation,
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
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationListResponse:
        """
        List invitations for an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of invitations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/organizations/{organization_id}/invitations",
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
                    invitation_list_params.InvitationListParams,
                ),
            ),
            cast_to=InvitationListResponse,
        )

    def delete(
        self,
        invitation_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an invitation

        Args:
          organization_id: Organization ID or label identifier

          invitation_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers.update({"Authorization": omit})
        return self._delete(
            f"/organizations/{organization_id}/invitations/{invitation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrganizationRole | Omit = omit,
        x_client_request_id: str | Omit = omit,
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """
        Create an invitation to join an organization

        Args:
          organization_id: Organization ID or label identifier

          email: Email address to invite

          role: Role to assign when invitation is accepted (defaults to org_admin if not
              provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._post(
            f"/organizations/{organization_id}/invitations",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invitation,
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
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationListResponse:
        """
        List invitations for an organization

        Args:
          organization_id: Organization ID or label identifier

          after: Cursor for forward pagination

          before: Cursor for backward pagination

          expand: Fields to expand in the response. Currently supports "permissions" to include
              the permissions field with the caller's permissions for the resource.

          limit: Maximum number of invitations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/organizations/{organization_id}/invitations",
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
                    invitation_list_params.InvitationListParams,
                ),
            ),
            cast_to=InvitationListResponse,
        )

    async def delete(
        self,
        invitation_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        x_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an invitation

        Args:
          organization_id: Organization ID or label identifier

          invitation_id: Identifier for API resources. A 26-char nanoid (URL/DNS safe).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-Client-Request-ID": x_client_request_id,
                    "X-Request-ID": x_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers.update({"Authorization": omit})
        return await self._delete(
            f"/organizations/{organization_id}/invitations/{invitation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_raw_response_wrapper(
            invitations.create,
        )
        self.list = to_raw_response_wrapper(
            invitations.list,
        )
        self.delete = to_raw_response_wrapper(
            invitations.delete,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_raw_response_wrapper(
            invitations.create,
        )
        self.list = async_to_raw_response_wrapper(
            invitations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invitations.delete,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = to_streamed_response_wrapper(
            invitations.list,
        )
        self.delete = to_streamed_response_wrapper(
            invitations.delete,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            invitations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invitations.delete,
        )
