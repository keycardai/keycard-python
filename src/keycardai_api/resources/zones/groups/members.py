# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zones.groups import member_add_params, member_list_params
from ....types.zones.groups.group_member import GroupMember
from ....types.zones.groups.member_list_response import MemberListResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        group_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """Returns a paginated list of the group's members.

        Use cursor pagination via
        `after`/`before`. Pass `expand[]=user` to embed each member's full user record
        and `expand[]=total_count` to include the matching row count. Pass `query[]`
        (repeatable, 1-255 chars) to search members by their user's email or federated
        credential subject (substring match, OR'd across repeated values). Pass
        `filter[id]` (repeatable, max 100) to restrict results to a known set of members
        by user ID — mutually exclusive with `after`/`before` (returns 400 if combined).
        When `filter[id]` is set, `limit` is ignored and the response contains every
        requested member that exists in the group, in a single page. IDs not in the
        group are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to the member with this user ID. Repeatable, max 100. Mutually
              exclusive with after/before.

          limit: Maximum number of items to return

          query: Search members by their user's email or federated credential subject (substring
              match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/groups/{group_id}/members", zone_id=zone_id, group_id=group_id),
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
                        "filter_id": filter_id,
                        "limit": limit,
                        "query": query,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    def add(
        self,
        group_id: str,
        *,
        zone_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMember:
        """Adds a user to a group managed in Keycard.

        Membership of externally synced
        groups is not managed manually.

        Args:
          user_id: ID of the user to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/groups/{group_id}/members", zone_id=zone_id, group_id=group_id),
            body=maybe_transform({"user_id": user_id}, member_add_params.MemberAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMember,
        )

    def remove(
        self,
        user_id: str,
        *,
        zone_id: str,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a user from a group managed in Keycard.

        Membership of externally synced
        groups is not managed manually. A member is identified by its user's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/zones/{zone_id}/groups/{group_id}/members/{user_id}",
                zone_id=zone_id,
                group_id=group_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        group_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """Returns a paginated list of the group's members.

        Use cursor pagination via
        `after`/`before`. Pass `expand[]=user` to embed each member's full user record
        and `expand[]=total_count` to include the matching row count. Pass `query[]`
        (repeatable, 1-255 chars) to search members by their user's email or federated
        credential subject (substring match, OR'd across repeated values). Pass
        `filter[id]` (repeatable, max 100) to restrict results to a known set of members
        by user ID — mutually exclusive with `after`/`before` (returns 400 if combined).
        When `filter[id]` is set, `limit` is ignored and the response contains every
        requested member that exists in the group, in a single page. IDs not in the
        group are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to the member with this user ID. Repeatable, max 100. Mutually
              exclusive with after/before.

          limit: Maximum number of items to return

          query: Search members by their user's email or federated credential subject (substring
              match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/groups/{group_id}/members", zone_id=zone_id, group_id=group_id),
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
                        "filter_id": filter_id,
                        "limit": limit,
                        "query": query,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    async def add(
        self,
        group_id: str,
        *,
        zone_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMember:
        """Adds a user to a group managed in Keycard.

        Membership of externally synced
        groups is not managed manually.

        Args:
          user_id: ID of the user to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/groups/{group_id}/members", zone_id=zone_id, group_id=group_id),
            body=await async_maybe_transform({"user_id": user_id}, member_add_params.MemberAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMember,
        )

    async def remove(
        self,
        user_id: str,
        *,
        zone_id: str,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a user from a group managed in Keycard.

        Membership of externally synced
        groups is not managed manually. A member is identified by its user's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/zones/{zone_id}/groups/{group_id}/members/{user_id}",
                zone_id=zone_id,
                group_id=group_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.add = to_raw_response_wrapper(
            members.add,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.add = async_to_raw_response_wrapper(
            members.add,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.add = to_streamed_response_wrapper(
            members.add,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.add = async_to_streamed_response_wrapper(
            members.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )
