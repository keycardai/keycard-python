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
from ....types.zones.groups import role_add_params, role_list_params, role_remove_params
from ....types.zones.users.role_assignment import RoleAssignment
from ....types.zones.groups.role_list_response import RoleListResponse

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def list(
        self,
        group_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles assigned to the group.

        Members inherit these roles. Returns
        the shared role-assignment shape with `principal_type` set to `group`. Use
        cursor pagination via `after`/`before`; pass `expand[]=total_count` to include
        the matching row count. Pass `filter[id]` (repeatable, max 100) to restrict
        results to a known set of role assignments, mutually exclusive with
        `after`/`before` (returns 400 if combined). When `filter[id]` is set, `limit` is
        ignored and the response contains every requested assignment that exists on the
        group, in a single page. IDs not on the group are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to the role assignment with this ID. Repeatable, max 100.
              Mutually exclusive with after/before.

          limit: Maximum number of items to return

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
            path_template("/zones/{zone_id}/groups/{group_id}/roles", zone_id=zone_id, group_id=group_id),
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
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    def add(
        self,
        group_id: str,
        *,
        zone_id: str,
        owner_type: Literal["platform", "customer"] | Omit = omit,
        role_id: str | Omit = omit,
        role_identifier: str | Omit = omit,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignment:
        """Assigns a role to the group; members inherit it.

        Provide role_id, or
        role_identifier with owner_type. Returns the shared role-assignment shape with
        `principal_type` set to `group`.

        Args:
          owner_type: Owner type of the role to assign. Required with role_identifier (an identifier
              is unique only per owner type); must be omitted with role_id.

          role_id: ID of the role to assign. Provide exactly one of role_id or role_identifier;
              owner_type must be omitted when role_id is used.

          role_identifier: Role identifier: a lowercase slug (letters and digits separated by single
              hyphens or underscores), unique per owner type within a zone. Role identifiers
              surface in policy evaluation, so the slug restriction keeps them unambiguous in
              policy text.

          scope_id: The ID of the resource to scope the grant to. Provide together with scope_type,
              or omit both for an unscoped assignment. When scope_type is `zone`, this must
              reference a different zone in the same organization.

          scope_type: The kind of resource to scope the grant to (e.g. `zone`). Provide together with
              scope_id, or omit both for an unscoped assignment (applies to the owning zone
              itself). Only platform roles on the org zone may carry a scope.

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
            path_template("/zones/{zone_id}/groups/{group_id}/roles", zone_id=zone_id, group_id=group_id),
            body=maybe_transform(
                {
                    "owner_type": owner_type,
                    "role_id": role_id,
                    "role_identifier": role_identifier,
                    "scope_id": scope_id,
                    "scope_type": scope_type,
                },
                role_add_params.RoleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    def remove(
        self,
        role_id: str,
        *,
        zone_id: str,
        group_id: str,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a role from the group.

        Provide the same (scope_type, scope_id) pair the
        grant was created with, or omit both to revoke the unscoped grant.

        Args:
          scope_id: Scope target of the grant to revoke. Provide together with scope_type.

          scope_type: Scope kind of the grant to revoke. Provide together with scope_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/zones/{zone_id}/groups/{group_id}/roles/{role_id}",
                zone_id=zone_id,
                group_id=group_id,
                role_id=role_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "scope_id": scope_id,
                        "scope_type": scope_type,
                    },
                    role_remove_params.RoleRemoveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    async def list(
        self,
        group_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        filter_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles assigned to the group.

        Members inherit these roles. Returns
        the shared role-assignment shape with `principal_type` set to `group`. Use
        cursor pagination via `after`/`before`; pass `expand[]=total_count` to include
        the matching row count. Pass `filter[id]` (repeatable, max 100) to restrict
        results to a known set of role assignments, mutually exclusive with
        `after`/`before` (returns 400 if combined). When `filter[id]` is set, `limit` is
        ignored and the response contains every requested assignment that exists on the
        group, in a single page. IDs not on the group are silently omitted.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          filter_id: Restrict results to the role assignment with this ID. Repeatable, max 100.
              Mutually exclusive with after/before.

          limit: Maximum number of items to return

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
            path_template("/zones/{zone_id}/groups/{group_id}/roles", zone_id=zone_id, group_id=group_id),
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
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    async def add(
        self,
        group_id: str,
        *,
        zone_id: str,
        owner_type: Literal["platform", "customer"] | Omit = omit,
        role_id: str | Omit = omit,
        role_identifier: str | Omit = omit,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignment:
        """Assigns a role to the group; members inherit it.

        Provide role_id, or
        role_identifier with owner_type. Returns the shared role-assignment shape with
        `principal_type` set to `group`.

        Args:
          owner_type: Owner type of the role to assign. Required with role_identifier (an identifier
              is unique only per owner type); must be omitted with role_id.

          role_id: ID of the role to assign. Provide exactly one of role_id or role_identifier;
              owner_type must be omitted when role_id is used.

          role_identifier: Role identifier: a lowercase slug (letters and digits separated by single
              hyphens or underscores), unique per owner type within a zone. Role identifiers
              surface in policy evaluation, so the slug restriction keeps them unambiguous in
              policy text.

          scope_id: The ID of the resource to scope the grant to. Provide together with scope_type,
              or omit both for an unscoped assignment. When scope_type is `zone`, this must
              reference a different zone in the same organization.

          scope_type: The kind of resource to scope the grant to (e.g. `zone`). Provide together with
              scope_id, or omit both for an unscoped assignment (applies to the owning zone
              itself). Only platform roles on the org zone may carry a scope.

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
            path_template("/zones/{zone_id}/groups/{group_id}/roles", zone_id=zone_id, group_id=group_id),
            body=await async_maybe_transform(
                {
                    "owner_type": owner_type,
                    "role_id": role_id,
                    "role_identifier": role_identifier,
                    "scope_id": scope_id,
                    "scope_type": scope_type,
                },
                role_add_params.RoleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    async def remove(
        self,
        role_id: str,
        *,
        zone_id: str,
        group_id: str,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a role from the group.

        Provide the same (scope_type, scope_id) pair the
        grant was created with, or omit both to revoke the unscoped grant.

        Args:
          scope_id: Scope target of the grant to revoke. Provide together with scope_type.

          scope_type: Scope kind of the grant to revoke. Provide together with scope_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/zones/{zone_id}/groups/{group_id}/roles/{role_id}",
                zone_id=zone_id,
                group_id=group_id,
                role_id=role_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "scope_id": scope_id,
                        "scope_type": scope_type,
                    },
                    role_remove_params.RoleRemoveParams,
                ),
            ),
            cast_to=NoneType,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.add = to_raw_response_wrapper(
            roles.add,
        )
        self.remove = to_raw_response_wrapper(
            roles.remove,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.add = async_to_raw_response_wrapper(
            roles.add,
        )
        self.remove = async_to_raw_response_wrapper(
            roles.remove,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.add = to_streamed_response_wrapper(
            roles.add,
        )
        self.remove = to_streamed_response_wrapper(
            roles.remove,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.add = async_to_streamed_response_wrapper(
            roles.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            roles.remove,
        )
