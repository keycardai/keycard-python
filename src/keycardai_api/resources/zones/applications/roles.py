# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.zones.applications import role_list_params, role_assign_params, role_revoke_params
from ....types.zones.users.role_assignment import RoleAssignment
from ....types.zones.applications.role_list_response import RoleListResponse

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
        application_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles assigned to the specified application within the zone.

        The
        full result set is currently returned in a single page; the
        `after`/`before`/`limit` cursor parameters are reserved and not yet enforced,
        and `pagination` cursors are always null.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles", zone_id=zone_id, application_id=application_id
            ),
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
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    def assign(
        self,
        application_id: str,
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
        """Assigns a role to the application.

        Provide exactly one of role_id or
        role_identifier; when role_identifier is used, owner_type is required to
        disambiguate roles that share an identifier across owner types (and must be
        omitted with role_id). An optional (scope_type, scope_id) pair scopes the grant;
        only platform roles on the org zone may carry a scope, and a `zone` scope must
        reference a different zone in the same organization.

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles", zone_id=zone_id, application_id=application_id
            ),
            body=maybe_transform(
                {
                    "owner_type": owner_type,
                    "role_id": role_id,
                    "role_identifier": role_identifier,
                    "scope_id": scope_id,
                    "scope_type": scope_type,
                },
                role_assign_params.RoleAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    def revoke(
        self,
        role_id: str,
        *,
        zone_id: str,
        application_id: str,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a role from the application.

        Provide the same (scope_type, scope_id)
        pair the grant was created with, or omit both to revoke the unscoped grant.

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles/{role_id}",
                zone_id=zone_id,
                application_id=application_id,
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
                    role_revoke_params.RoleRevokeParams,
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
        application_id: str,
        *,
        zone_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles assigned to the specified application within the zone.

        The
        full result set is currently returned in a single page; the
        `after`/`before`/`limit` cursor parameters are reserved and not yet enforced,
        and `pagination` cursors are always null.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._get(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles", zone_id=zone_id, application_id=application_id
            ),
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
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    async def assign(
        self,
        application_id: str,
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
        """Assigns a role to the application.

        Provide exactly one of role_id or
        role_identifier; when role_identifier is used, owner_type is required to
        disambiguate roles that share an identifier across owner types (and must be
        omitted with role_id). An optional (scope_type, scope_id) pair scopes the grant;
        only platform roles on the org zone may carry a scope, and a `zone` scope must
        reference a different zone in the same organization.

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles", zone_id=zone_id, application_id=application_id
            ),
            body=await async_maybe_transform(
                {
                    "owner_type": owner_type,
                    "role_id": role_id,
                    "role_identifier": role_identifier,
                    "scope_id": scope_id,
                    "scope_type": scope_type,
                },
                role_assign_params.RoleAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignment,
        )

    async def revoke(
        self,
        role_id: str,
        *,
        zone_id: str,
        application_id: str,
        scope_id: str | Omit = omit,
        scope_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a role from the application.

        Provide the same (scope_type, scope_id)
        pair the grant was created with, or omit both to revoke the unscoped grant.

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/zones/{zone_id}/applications/{application_id}/roles/{role_id}",
                zone_id=zone_id,
                application_id=application_id,
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
                    role_revoke_params.RoleRevokeParams,
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
        self.assign = to_raw_response_wrapper(
            roles.assign,
        )
        self.revoke = to_raw_response_wrapper(
            roles.revoke,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.assign = async_to_raw_response_wrapper(
            roles.assign,
        )
        self.revoke = async_to_raw_response_wrapper(
            roles.revoke,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.assign = to_streamed_response_wrapper(
            roles.assign,
        )
        self.revoke = to_streamed_response_wrapper(
            roles.revoke,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            roles.assign,
        )
        self.revoke = async_to_streamed_response_wrapper(
            roles.revoke,
        )
