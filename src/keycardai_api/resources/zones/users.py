# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import user_list_params
from ..._base_client import make_request_options
from ...types.zones.user import User
from ...types.zones.user_list_response import UserListResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Returns details of a specific user by user ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/zones/{zone_id}/users/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        filter_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Returns a list of users in the specified zone.

        **Rollout note:** the paginated/searchable/sortable behavior described below is
        gated behind the `user-pagination` feature flag and is currently disabled for
        most zones. While the flag is off, the response returns every user in the zone
        (capped at 100) in `items` and a fixed pagination envelope where `after_cursor`
        and `before_cursor` are `null` and `total_count` is `0`. The query parameters
        below are accepted but ignored. The flag is rolled out per-zone in Datadog and
        will become the default once Console adopts the paginated contract.

        Use cursor pagination via `after`/`before`. Sort: comma-separated field list;
        prefix with `-` for descending. Use `expand[]=total_count` to include the
        matching row count. Filter by exact email via `filter[email]`; search via
        `query[email]` / `query[subject]` / `query[]` (substring match, OR'd across
        repeated values). `query[]` matches against email and federation credential
        subject. Pass `filter[id]` (repeatable, max 100) to restrict results to a known
        set of users — mutually exclusive with `after`/`before` (returns 400 if
        combined). When `filter[id]` is set, `limit` is ignored and the response
        contains every requested user that exists in the zone, in a single page. IDs not
        in the zone are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_email: Filter by exact email address

          filter_id: Restrict results to users with this publicId. Repeatable, max 100. Mutually
              exclusive with after/before.

          limit: Maximum number of items to return

          query: Search across email and credential subject (substring match)

          query_email: Search by email (substring match)

          query_subject: Search by federated credential subject (substring match)

          sort: Comma-separated sort fields. Prefix with - for descending. Allowed: created_at,
              email, authenticated_at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/users", zone_id=zone_id),
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
                        "filter_email": filter_email,
                        "filter_id": filter_id,
                        "limit": limit,
                        "query": query,
                        "query_email": query_email,
                        "query_subject": query_subject,
                        "sort": sort,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Returns details of a specific user by user ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/users/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        filter_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Returns a list of users in the specified zone.

        **Rollout note:** the paginated/searchable/sortable behavior described below is
        gated behind the `user-pagination` feature flag and is currently disabled for
        most zones. While the flag is off, the response returns every user in the zone
        (capped at 100) in `items` and a fixed pagination envelope where `after_cursor`
        and `before_cursor` are `null` and `total_count` is `0`. The query parameters
        below are accepted but ignored. The flag is rolled out per-zone in Datadog and
        will become the default once Console adopts the paginated contract.

        Use cursor pagination via `after`/`before`. Sort: comma-separated field list;
        prefix with `-` for descending. Use `expand[]=total_count` to include the
        matching row count. Filter by exact email via `filter[email]`; search via
        `query[email]` / `query[subject]` / `query[]` (substring match, OR'd across
        repeated values). `query[]` matches against email and federation credential
        subject. Pass `filter[id]` (repeatable, max 100) to restrict results to a known
        set of users — mutually exclusive with `after`/`before` (returns 400 if
        combined). When `filter[id]` is set, `limit` is ignored and the response
        contains every requested user that exists in the zone, in a single page. IDs not
        in the zone are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_email: Filter by exact email address

          filter_id: Restrict results to users with this publicId. Repeatable, max 100. Mutually
              exclusive with after/before.

          limit: Maximum number of items to return

          query: Search across email and credential subject (substring match)

          query_email: Search by email (substring match)

          query_subject: Search by federated credential subject (substring match)

          sort: Comma-separated sort fields. Prefix with - for descending. Allowed: created_at,
              email, authenticated_at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/users", zone_id=zone_id),
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
                        "filter_email": filter_email,
                        "filter_id": filter_id,
                        "limit": limit,
                        "query": query,
                        "query_email": query_email,
                        "query_subject": query_subject,
                        "sort": sort,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
