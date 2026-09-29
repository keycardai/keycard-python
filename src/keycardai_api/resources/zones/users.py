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
from ...types.zones import user_list_params, user_retrieve_params
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
        expand: Union[Literal["role-assignments", "groups"], List[Literal["role-assignments", "groups"]]] | Omit = omit,
        role_source: Literal["user", "group", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Returns details of a specific user by user ID.

        Use `expand[]=role-assignments`
        for the user's structured role grants and `expand[]=groups` for the user's group
        memberships. Role grants are direct only by default, each tagged with `source`;
        use `role_source=all` to also include group-inherited.

        Args:
          role_source: Selects which grants `expand[]=role-assignments` returns, tagging each with
              `source`: `user` (direct only, the default), `group` (group-inherited only), or
              `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "role_source": role_source,
                    },
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=User,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[
            Literal[
                "total_count",
                "session_count",
                "grant_count",
                "role-assignments",
                "groups",
                "credentials",
                "credentials.provider",
            ],
            List[
                Literal[
                    "total_count",
                    "session_count",
                    "grant_count",
                    "role-assignments",
                    "groups",
                    "credentials",
                    "credentials.provider",
                ]
            ],
        ]
        | Omit = omit,
        filter_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_external: bool | Omit = omit,
        filter_groups: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_identifier: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_issuer: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_role: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        role_source: Literal["user", "group", "all"] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Returns a paginated list of users in the specified zone.

        Use cursor pagination via `after`/`before`. Sort: comma-separated field list;
        prefix with `-` for descending. Use `expand[]=total_count` to include the
        matching row count, `expand[]=session_count` to include per-user session counts,
        `expand[]=grant_count` to include per-user delegated-grant counts,
        `expand[]=role-assignments` to include each user's structured role grants
        (direct grants only by default, each tagged with `source`; use `role_source=all`
        to also include group-inherited), `expand[]=groups` to include each user's group
        memberships, `expand[]=credentials` to include each user's authentication
        credentials (each with its `provider_id`), and `expand[]=credentials.provider`
        to additionally inline the full identity provider on each federation credential.
        Filter by exact email via `filter[email]` and by exact identifier via
        `filter[identifier]`; restrict to members of a group via `filter[groups]`
        (repeatable, OR'd across values); restrict to users directly granted a role via
        `filter[role]` (role identifier, repeatable up to 100, OR'd across values;
        group-inherited grants do not match); pass `filter[external]=false` for only
        users managed in Keycard or `filter[external]=true` for only users provisioned
        by an external directory (omit to list both); match exactly on the user's
        `subject` and `issuer` via `filter[subject]` and `filter[issuer]` (each
        repeatable and OR'd across values; AND'd with each other); search via
        `query[email]` / `query[subject]` / `query[]` (substring match, OR'd across
        repeated values). `query[]` matches against email and the user's `subject`. Pass
        `filter[id]` (repeatable, max 100) to restrict results to a known set of users —
        mutually exclusive with `after`/`before` (returns 400 if combined). When
        `filter[id]` is set, `limit` is ignored and the response contains every
        requested user that exists in the zone, in a single page. IDs not in the zone
        are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_email: Filter by exact email address

          filter_external: Filter by source: `false` for users managed in Keycard, `true` for users
              provisioned by an external directory. Omit to list both.

          filter_groups: Restrict to members of this group (by group ID). Repeatable; OR'd across values.

          filter_id: Restrict results to users with this publicId. Repeatable, max 100. Mutually
              exclusive with after/before.

          filter_identifier: Filter by exact user identifier

          filter_issuer: Filter by exact `issuer`. Repeatable; OR'd across values.

          filter_role: Restrict to users directly granted this role (by role identifier). Repeatable,
              max 100; OR'd across values. Group-inherited grants do not match.

          filter_subject: Filter by exact `subject`. Repeatable; OR'd across values.

          limit: Maximum number of items to return

          query: Search across email and the user's `subject` (substring match)

          query_email: Search by email (substring match)

          query_subject: Search by the user's `subject` (substring match)

          role_source: Selects which grants `expand[]=role-assignments` returns, tagging each with
              `source`: `user` (direct only, the default), `group` (group-inherited only), or
              `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.

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
                        "filter_external": filter_external,
                        "filter_groups": filter_groups,
                        "filter_id": filter_id,
                        "filter_identifier": filter_identifier,
                        "filter_issuer": filter_issuer,
                        "filter_role": filter_role,
                        "filter_subject": filter_subject,
                        "limit": limit,
                        "query": query,
                        "query_email": query_email,
                        "query_subject": query_subject,
                        "role_source": role_source,
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
        expand: Union[Literal["role-assignments", "groups"], List[Literal["role-assignments", "groups"]]] | Omit = omit,
        role_source: Literal["user", "group", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Returns details of a specific user by user ID.

        Use `expand[]=role-assignments`
        for the user's structured role grants and `expand[]=groups` for the user's group
        memberships. Role grants are direct only by default, each tagged with `source`;
        use `role_source=all` to also include group-inherited.

        Args:
          role_source: Selects which grants `expand[]=role-assignments` returns, tagging each with
              `source`: `user` (direct only, the default), `group` (group-inherited only), or
              `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "role_source": role_source,
                    },
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=User,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[
            Literal[
                "total_count",
                "session_count",
                "grant_count",
                "role-assignments",
                "groups",
                "credentials",
                "credentials.provider",
            ],
            List[
                Literal[
                    "total_count",
                    "session_count",
                    "grant_count",
                    "role-assignments",
                    "groups",
                    "credentials",
                    "credentials.provider",
                ]
            ],
        ]
        | Omit = omit,
        filter_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_external: bool | Omit = omit,
        filter_groups: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_identifier: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_issuer: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_role: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_email: Union[str, SequenceNotStr[str]] | Omit = omit,
        query_subject: Union[str, SequenceNotStr[str]] | Omit = omit,
        role_source: Literal["user", "group", "all"] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Returns a paginated list of users in the specified zone.

        Use cursor pagination via `after`/`before`. Sort: comma-separated field list;
        prefix with `-` for descending. Use `expand[]=total_count` to include the
        matching row count, `expand[]=session_count` to include per-user session counts,
        `expand[]=grant_count` to include per-user delegated-grant counts,
        `expand[]=role-assignments` to include each user's structured role grants
        (direct grants only by default, each tagged with `source`; use `role_source=all`
        to also include group-inherited), `expand[]=groups` to include each user's group
        memberships, `expand[]=credentials` to include each user's authentication
        credentials (each with its `provider_id`), and `expand[]=credentials.provider`
        to additionally inline the full identity provider on each federation credential.
        Filter by exact email via `filter[email]` and by exact identifier via
        `filter[identifier]`; restrict to members of a group via `filter[groups]`
        (repeatable, OR'd across values); restrict to users directly granted a role via
        `filter[role]` (role identifier, repeatable up to 100, OR'd across values;
        group-inherited grants do not match); pass `filter[external]=false` for only
        users managed in Keycard or `filter[external]=true` for only users provisioned
        by an external directory (omit to list both); match exactly on the user's
        `subject` and `issuer` via `filter[subject]` and `filter[issuer]` (each
        repeatable and OR'd across values; AND'd with each other); search via
        `query[email]` / `query[subject]` / `query[]` (substring match, OR'd across
        repeated values). `query[]` matches against email and the user's `subject`. Pass
        `filter[id]` (repeatable, max 100) to restrict results to a known set of users —
        mutually exclusive with `after`/`before` (returns 400 if combined). When
        `filter[id]` is set, `limit` is ignored and the response contains every
        requested user that exists in the zone, in a single page. IDs not in the zone
        are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_email: Filter by exact email address

          filter_external: Filter by source: `false` for users managed in Keycard, `true` for users
              provisioned by an external directory. Omit to list both.

          filter_groups: Restrict to members of this group (by group ID). Repeatable; OR'd across values.

          filter_id: Restrict results to users with this publicId. Repeatable, max 100. Mutually
              exclusive with after/before.

          filter_identifier: Filter by exact user identifier

          filter_issuer: Filter by exact `issuer`. Repeatable; OR'd across values.

          filter_role: Restrict to users directly granted this role (by role identifier). Repeatable,
              max 100; OR'd across values. Group-inherited grants do not match.

          filter_subject: Filter by exact `subject`. Repeatable; OR'd across values.

          limit: Maximum number of items to return

          query: Search across email and the user's `subject` (substring match)

          query_email: Search by email (substring match)

          query_subject: Search by the user's `subject` (substring match)

          role_source: Selects which grants `expand[]=role-assignments` returns, tagging each with
              `source`: `user` (direct only, the default), `group` (group-inherited only), or
              `all` (both direct and group-inherited). Requires `expand[]=role-assignments`.

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
                        "filter_external": filter_external,
                        "filter_groups": filter_groups,
                        "filter_id": filter_id,
                        "filter_identifier": filter_identifier,
                        "filter_issuer": filter_issuer,
                        "filter_role": filter_role,
                        "filter_subject": filter_subject,
                        "limit": limit,
                        "query": query,
                        "query_email": query_email,
                        "query_subject": query_subject,
                        "role_source": role_source,
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
