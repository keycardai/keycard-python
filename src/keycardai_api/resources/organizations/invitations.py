# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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
from ...types.organizations import OrganizationRole, invitation_list_params, invitation_create_params
from ...types.organizations.invitation import Invitation
from ...types.organizations.invitation_status import InvitationStatus
from ...types.organizations.organization_role import OrganizationRole
from ...types.organizations.invitation_list_response import InvitationListResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrganizationRole,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """Create an invitation to join an organization and queue the invitation email.

        The
        invitation is created even when the email service cannot be reached; the
        response's `delivery_status` is `failed` then, no email was queued, and the
        caller must resend. A 4xx from the email service, such as a recipient send cap,
        creates no invitation.

        Args:
          organization_id: Organization ID or label identifier

          email: Email address to invite

          role: Role to assign when invitation is accepted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            path_template("/organizations/{organization_id}/invitations", organization_id=organization_id),
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
        expand: Union[Literal["permissions", "total_count"], List[Literal["permissions", "total_count"]]] | Omit = omit,
        filter_status: List[InvitationStatus] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
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

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For the
              service account and service account credential list operations, "total_count"
              populates pagination.total_count with the number of items matching the same
              filters as the list (excluding cursor and limit). Other operations ignore expand
              values they do not use.

          filter_status: Return only invitations with these statuses. Repeat the parameter to match any
              of several statuses (`?filter[status]=pending&filter[status]=accepted`). Expired
              invitations are never listed, so `expired` matches nothing. When absent, no
              status filter is applied.

          limit: Maximum number of invitations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._get(
            path_template("/organizations/{organization_id}/invitations", organization_id=organization_id),
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
                        "filter_status": filter_status,
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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/organizations/{organization_id}/invitations/{invitation_id}",
                organization_id=organization_id,
                invitation_id=invitation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resend(
        self,
        invitation_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """Send a fresh invitation email.

        The invitation token is rotated, so the link in
        any earlier email stops working. Returns 409 while a previous email is still
        queued or sending, or when the invitation is no longer pending. Returns 200 even
        when the email service cannot be reached: the token has already been rotated,
        the response's `delivery_status` is `failed`, no new email was queued, and the
        caller must resend. Each resend counts toward the organization's daily
        invitation limit. Returns 429 with a `Retry-After` header when that limit or the
        per-recipient send cap is reached. If the email service rejects the send, the
        earlier link keeps working.

        After the organization access check succeeds, the service sends
        `X-Should-Retry: false` on 409, 429, and 5xx responses to tell SDKs to surface
        the error without retrying. A retry can rotate the token and invalidate an email
        link, including when the first send succeeded but the response did not reach the
        caller.

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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._post(
            path_template(
                "/organizations/{organization_id}/invitations/{invitation_id}/resend",
                organization_id=organization_id,
                invitation_id=invitation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invitation,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrganizationRole,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """Create an invitation to join an organization and queue the invitation email.

        The
        invitation is created even when the email service cannot be reached; the
        response's `delivery_status` is `failed` then, no email was queued, and the
        caller must resend. A 4xx from the email service, such as a recipient send cap,
        creates no invitation.

        Args:
          organization_id: Organization ID or label identifier

          email: Email address to invite

          role: Role to assign when invitation is accepted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/organizations/{organization_id}/invitations", organization_id=organization_id),
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
        expand: Union[Literal["permissions", "total_count"], List[Literal["permissions", "total_count"]]] | Omit = omit,
        filter_status: List[InvitationStatus] | Omit = omit,
        limit: int | Omit = omit,
        x_client_request_id: str | Omit = omit,
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

          expand: Fields to expand in the response. Supports "permissions" to include the
              permissions field with the caller's permissions for the resource. For the
              service account and service account credential list operations, "total_count"
              populates pagination.total_count with the number of items matching the same
              filters as the list (excluding cursor and limit). Other operations ignore expand
              values they do not use.

          filter_status: Return only invitations with these statuses. Repeat the parameter to match any
              of several statuses (`?filter[status]=pending&filter[status]=accepted`). Expired
              invitations are never listed, so `expired` matches nothing. When absent, no
              status filter is applied.

          limit: Maximum number of invitations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/organizations/{organization_id}/invitations", organization_id=organization_id),
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
                        "filter_status": filter_status,
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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/organizations/{organization_id}/invitations/{invitation_id}",
                organization_id=organization_id,
                invitation_id=invitation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resend(
        self,
        invitation_id: str,
        *,
        organization_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invitation:
        """Send a fresh invitation email.

        The invitation token is rotated, so the link in
        any earlier email stops working. Returns 409 while a previous email is still
        queued or sending, or when the invitation is no longer pending. Returns 200 even
        when the email service cannot be reached: the token has already been rotated,
        the response's `delivery_status` is `failed`, no new email was queued, and the
        caller must resend. Each resend counts toward the organization's daily
        invitation limit. Returns 429 with a `Retry-After` header when that limit or the
        per-recipient send cap is reached. If the email service rejects the send, the
        earlier link keeps working.

        After the organization access check succeeds, the service sends
        `X-Should-Retry: false` on 409, 429, and 5xx responses to tell SDKs to surface
        the error without retrying. A retry can rotate the token and invalidate an email
        link, including when the first send succeeded but the response did not reach the
        caller.

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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._post(
            path_template(
                "/organizations/{organization_id}/invitations/{invitation_id}/resend",
                organization_id=organization_id,
                invitation_id=invitation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invitation,
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
        self.resend = to_raw_response_wrapper(
            invitations.resend,
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
        self.resend = async_to_raw_response_wrapper(
            invitations.resend,
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
        self.resend = to_streamed_response_wrapper(
            invitations.resend,
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
        self.resend = async_to_streamed_response_wrapper(
            invitations.resend,
        )
