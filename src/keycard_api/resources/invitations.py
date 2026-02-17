# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.invitation_accept_response import InvitationAcceptResponse
from ..types.invitation_retrieve_response import InvitationRetrieveResponse

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

    def retrieve(
        self,
        token: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """
        View invitation details by token without consuming the token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/invitations/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    def accept(
        self,
        token: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationAcceptResponse:
        """
        Accept and consume an invitation token to join the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._post(
            f"/invitations/{token}/accept",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationAcceptResponse,
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

    async def retrieve(
        self,
        token: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """
        View invitation details by token without consuming the token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/invitations/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    async def accept(
        self,
        token: str,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationAcceptResponse:
        """
        Accept and consume an invitation token to join the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._post(
            f"/invitations/{token}/accept",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationAcceptResponse,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.accept = to_raw_response_wrapper(
            invitations.accept,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = async_to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.accept = async_to_raw_response_wrapper(
            invitations.accept,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.accept = to_streamed_response_wrapper(
            invitations.accept,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = async_to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.accept = async_to_streamed_response_wrapper(
            invitations.accept,
        )
