# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import role_list_params, role_create_params, role_update_params
from ..._base_client import make_request_options
from ...types.zones.role import Role
from ...types.zones.role_list_response import RoleListResponse

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

    def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Creates a new customer-owned role in the specified zone.

        The owner_type is
        always customer; platform roles are managed by Keycard.

        Args:
          identifier: Role identifier: a lowercase slug (letters and digits separated by single
              hyphens or underscores), unique per owner type within a zone. Role identifiers
              surface in policy evaluation, so the slug restriction keeps them unambiguous in
              policy text.

          description: Human-readable description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/roles", zone_id=zone_id),
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "description": description,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def retrieve(
        self,
        role_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """
        Returns details of a specific role by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def update(
        self,
        role_id: str,
        *,
        zone_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Updates a customer-owned role's description.

        The identifier is immutable, and
        platform-owned roles cannot be modified.

        Args:
          description: Human-readable description (set to null to unset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            body=maybe_transform({"description": description}, role_update_params.RoleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles defined in the specified zone.

        The full result set is
        currently returned in a single page; the `after`/`before`/`limit` cursor
        parameters are reserved and not yet enforced, and `pagination` cursors are
        always null.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          identifier: Filter roles by identifier

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/roles", zone_id=zone_id),
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
                        "identifier": identifier,
                        "limit": limit,
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    def delete(
        self,
        role_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a customer-owned role.

        Platform-owned roles cannot be
        deleted, and a role with existing assignments returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Creates a new customer-owned role in the specified zone.

        The owner_type is
        always customer; platform roles are managed by Keycard.

        Args:
          identifier: Role identifier: a lowercase slug (letters and digits separated by single
              hyphens or underscores), unique per owner type within a zone. Role identifiers
              surface in policy evaluation, so the slug restriction keeps them unambiguous in
              policy text.

          description: Human-readable description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/roles", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "description": description,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def retrieve(
        self,
        role_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """
        Returns details of a specific role by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def update(
        self,
        role_id: str,
        *,
        zone_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Updates a customer-owned role's description.

        The identifier is immutable, and
        platform-owned roles cannot be modified.

        Args:
          description: Human-readable description (set to null to unset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            body=await async_maybe_transform({"description": description}, role_update_params.RoleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """Returns the roles defined in the specified zone.

        The full result set is
        currently returned in a single page; the `after`/`before`/`limit` cursor
        parameters are reserved and not yet enforced, and `pagination` cursors are
        always null.

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          identifier: Filter roles by identifier

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/roles", zone_id=zone_id),
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
                        "identifier": identifier,
                        "limit": limit,
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            cast_to=RoleListResponse,
        )

    async def delete(
        self,
        role_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a customer-owned role.

        Platform-owned roles cannot be
        deleted, and a role with existing assignments returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/zones/{zone_id}/roles/{role_id}", zone_id=zone_id, role_id=role_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            roles.update,
        )
        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.delete = to_raw_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            roles.update,
        )
        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            roles.delete,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            roles.update,
        )
        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.delete = to_streamed_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            roles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            roles.delete,
        )
