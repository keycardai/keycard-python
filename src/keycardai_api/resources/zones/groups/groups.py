# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from .roles import (
    RolesResource,
    AsyncRolesResource,
    RolesResourceWithRawResponse,
    AsyncRolesResourceWithRawResponse,
    RolesResourceWithStreamingResponse,
    AsyncRolesResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from ....types.zones import group_list_params, group_create_params, group_update_params, group_retrieve_params
from ...._base_client import make_request_options
from ....types.zones.group import Group
from ....types.zones.group_list_response import GroupListResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def roles(self) -> RolesResource:
        return RolesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        name: str,
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Creates a group in the zone (managed in Keycard).

        Groups synced from an external
        directory are created by that directory, not here.

        Args:
          name: Human-readable group name

          identifier: User-specified identifier, unique within the zone. Derived from the name when
              omitted (a suffix is appended if it collides).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/groups", zone_id=zone_id),
            body=maybe_transform(
                {
                    "name": name,
                    "identifier": identifier,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def retrieve(
        self,
        group_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["member_count", "roles"], List[Literal["member_count", "roles"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Returns a group by ID.

        Pass `expand[]=member_count` for its member count and
        `expand[]=roles` for the identifiers of its assigned roles.

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
        return self._get(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, group_retrieve_params.GroupRetrieveParams),
            ),
            cast_to=Group,
        )

    def update(
        self,
        group_id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Updates a group's name and/or identifier (partial update).

        A group's source is
        immutable. The name of a group synced from an external directory cannot be
        changed while external sync is enabled for the zone; its identifier can.

        Args:
          identifier: User-specified identifier, unique within the zone.

          name: Human-readable group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[
            Literal["total_count", "member_count", "roles"], List[Literal["total_count", "member_count", "roles"]]
        ]
        | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_identifier: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupListResponse:
        """Returns a paginated list of the groups in the specified zone.

        Use cursor
        pagination via `after`/`before`. Sort: comma-separated field list; prefix with
        `-` for descending (allowed: created_at, name, identifier). Pass
        `expand[]=member_count` to include each group's member count, `expand[]=roles`
        to include the identifiers of the roles assigned to each group, and
        `expand[]=total_count` to include the matching row count. Filter by exact
        identifier via `filter[identifier]` (repeatable, OR'd across values). Search via
        `query[]` (case-insensitive substring match, OR'd across repeated values); it
        matches the group's name and identifier. Pass `filter[id]` (repeatable, max 100)
        to restrict results to a known set of groups — mutually exclusive with
        `after`/`before` (returns 400 if combined). When `filter[id]` is set, `limit` is
        ignored and the response contains every requested group that exists in the zone,
        in a single page. IDs not in the zone are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to groups with this ID. Repeatable, max 100. Mutually exclusive
              with after/before.

          filter_identifier: Filter by exact group identifier

          limit: Maximum number of items to return

          query: Search across name and identifier (substring match)

          sort: Comma-separated sort fields. Prefix with - for descending. Allowed: created_at,
              name, identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/groups", zone_id=zone_id),
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
                        "filter_identifier": filter_identifier,
                        "limit": limit,
                        "query": query,
                        "sort": sort,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    def delete(
        self,
        group_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a group and its memberships and role assignments.

        Groups synced from an
        external directory can only be deleted by that directory (after external sync is
        disabled).

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        return AsyncRolesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        name: str,
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Creates a group in the zone (managed in Keycard).

        Groups synced from an external
        directory are created by that directory, not here.

        Args:
          name: Human-readable group name

          identifier: User-specified identifier, unique within the zone. Derived from the name when
              omitted (a suffix is appended if it collides).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/groups", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "identifier": identifier,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def retrieve(
        self,
        group_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["member_count", "roles"], List[Literal["member_count", "roles"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Returns a group by ID.

        Pass `expand[]=member_count` for its member count and
        `expand[]=roles` for the identifiers of its assigned roles.

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
        return await self._get(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, group_retrieve_params.GroupRetrieveParams),
            ),
            cast_to=Group,
        )

    async def update(
        self,
        group_id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """Updates a group's name and/or identifier (partial update).

        A group's source is
        immutable. The name of a group synced from an external directory cannot be
        changed while external sync is enabled for the zone; its identifier can.

        Args:
          identifier: User-specified identifier, unique within the zone.

          name: Human-readable group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[
            Literal["total_count", "member_count", "roles"], List[Literal["total_count", "member_count", "roles"]]
        ]
        | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        filter_identifier: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        query: Union[str, SequenceNotStr[str]] | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupListResponse:
        """Returns a paginated list of the groups in the specified zone.

        Use cursor
        pagination via `after`/`before`. Sort: comma-separated field list; prefix with
        `-` for descending (allowed: created_at, name, identifier). Pass
        `expand[]=member_count` to include each group's member count, `expand[]=roles`
        to include the identifiers of the roles assigned to each group, and
        `expand[]=total_count` to include the matching row count. Filter by exact
        identifier via `filter[identifier]` (repeatable, OR'd across values). Search via
        `query[]` (case-insensitive substring match, OR'd across repeated values); it
        matches the group's name and identifier. Pass `filter[id]` (repeatable, max 100)
        to restrict results to a known set of groups — mutually exclusive with
        `after`/`before` (returns 400 if combined). When `filter[id]` is set, `limit` is
        ignored and the response contains every requested group that exists in the zone,
        in a single page. IDs not in the zone are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to groups with this ID. Repeatable, max 100. Mutually exclusive
              with after/before.

          filter_identifier: Filter by exact group identifier

          limit: Maximum number of items to return

          query: Search across name and identifier (substring match)

          sort: Comma-separated sort fields. Prefix with - for descending. Allowed: created_at,
              name, identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/groups", zone_id=zone_id),
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
                        "filter_identifier": filter_identifier,
                        "limit": limit,
                        "query": query,
                        "sort": sort,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    async def delete(
        self,
        group_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a group and its memberships and role assignments.

        Groups synced from an
        external directory can only be deleted by that directory (after external sync is
        disabled).

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/zones/{zone_id}/groups/{group_id}", zone_id=zone_id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._groups.members)

    @cached_property
    def roles(self) -> RolesResourceWithRawResponse:
        return RolesResourceWithRawResponse(self._groups.roles)


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._groups.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithRawResponse:
        return AsyncRolesResourceWithRawResponse(self._groups.roles)


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._groups.members)

    @cached_property
    def roles(self) -> RolesResourceWithStreamingResponse:
        return RolesResourceWithStreamingResponse(self._groups.roles)


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._groups.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithStreamingResponse:
        return AsyncRolesResourceWithStreamingResponse(self._groups.roles)
