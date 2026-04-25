# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.zones import policy_set_list_params, policy_set_create_params, policy_set_update_params
from ...._base_client import make_request_options
from ....types.zones.policy_set_with_binding import PolicySetWithBinding
from ....types.zones.policy_set_list_response import PolicySetListResponse

__all__ = ["PolicySetsResource", "AsyncPolicySetsResource"]


class PolicySetsResource(SyncAPIResource):
    """Policy set CRUD and binding management"""

    @cached_property
    def versions(self) -> VersionsResource:
        """Immutable policy set manifest snapshots"""
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicySetsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        name: str,
        scope_type: Literal["zone", "resource", "user", "session"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Creates an unbound policy set.

        Use updatePolicySet to bind after creating a
        version.

        Args:
          scope_type:
              The scope at which this policy set applies:

              - `"zone"` — applies to all requests in the zone.
              - `"resource"` — scoped to a specific resource.
              - `"user"` — scoped to a specific user.
              - `"session"` — scoped to a specific session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/zones/{zone_id}/policy-sets", zone_id=zone_id),
            body=maybe_transform(
                {
                    "name": name,
                    "scope_type": scope_type,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Returns the policy set with current binding information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        name: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Update metadata or manage binding.

        Set active=true to bind, active=false to
        unbind.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            body=maybe_transform({"name": name}, policy_set_update_params.PolicySetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    def list(
        self,
        zone_id: str,
        *,
        active: bool | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_active: bool | Omit = omit,
        filter_owner_type: SequenceNotStr[str] | Omit = omit,
        filter_scope_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query: SequenceNotStr[str] | Omit = omit,
        query_name: SequenceNotStr[str] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetListResponse:
        """
        List policy sets in a zone

        Args:
          active: **Deprecated.** Use `filter[active]` instead.

              Filter by active binding status. When `true`, returns only policy sets with an
              active binding. When `false`, returns only policy sets without one. Omit to
              return all.

              Still honored for backward compatibility. Supplying both `active` and
              `filter[active]` with conflicting values returns `400 Bad Request`.

          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: **Deprecated.** Use `expand[]` instead.

              Opt-in to additional response fields. Still honored for backward compatibility;
              supplying both `expand` and `expand[]` with disagreeing values returns
              `400 Bad Request`.

          filter_active: Filter by active binding status. When `true`, returns only policy sets with an
              active binding. When `false`, returns only policy sets without one. Omit to
              return all.

          filter_owner_type: Filter on `owner_type`. Repeatable; repeated instances OR across values (e.g.
              `?filter[owner_type]=platform&filter[owner_type]=customer` matches either). See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `platform`, `customer`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values (e.g.
              `?filter[owner_type]=platform,customer`) are rejected with a 400 pointing at the
              repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          filter_scope_type: Filter on `scope_type` (policy sets only). Repeatable; repeated instances OR
              across values. See `FilterValues` in the shared spec for the full wire
              convention.

              Allowed values: `zone`, `resource`, `user`, `session`. Unknown values return 400
              with the list of allowed values. Comma-separated single values are rejected with
              a 400 pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query: Case-insensitive substring search across all searchable fields of the resource.
              For policies that is `name` and `description`; for policy sets that is `name`.
              Repeatable; if multiple terms are supplied they are OR-ed.

          query_name: Case-insensitive substring search on `name`. Repeatable; if multiple terms are
              supplied they are OR-ed (any matching term returns the row).

          sort: Field to sort by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/zones/{zone_id}/policy-sets", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "before": before,
                        "expand": expand,
                        "filter_active": filter_active,
                        "filter_owner_type": filter_owner_type,
                        "filter_scope_type": filter_scope_type,
                        "limit": limit,
                        "order": order,
                        "query": query,
                        "query_name": query_name,
                        "sort": sort,
                    },
                    policy_set_list_params.PolicySetListParams,
                ),
            ),
            cast_to=PolicySetListResponse,
        )

    def archive(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Archive a policy set

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )


class AsyncPolicySetsResource(AsyncAPIResource):
    """Policy set CRUD and binding management"""

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicySetsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        name: str,
        scope_type: Literal["zone", "resource", "user", "session"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Creates an unbound policy set.

        Use updatePolicySet to bind after creating a
        version.

        Args:
          scope_type:
              The scope at which this policy set applies:

              - `"zone"` — applies to all requests in the zone.
              - `"resource"` — scoped to a specific resource.
              - `"user"` — scoped to a specific user.
              - `"session"` — scoped to a specific session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/zones/{zone_id}/policy-sets", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scope_type": scope_type,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    async def retrieve(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Returns the policy set with current binding information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    async def update(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        name: str | Omit = omit,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """Update metadata or manage binding.

        Set active=true to bind, active=false to
        unbind.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            body=await async_maybe_transform({"name": name}, policy_set_update_params.PolicySetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )

    async def list(
        self,
        zone_id: str,
        *,
        active: bool | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_active: bool | Omit = omit,
        filter_owner_type: SequenceNotStr[str] | Omit = omit,
        filter_scope_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query: SequenceNotStr[str] | Omit = omit,
        query_name: SequenceNotStr[str] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetListResponse:
        """
        List policy sets in a zone

        Args:
          active: **Deprecated.** Use `filter[active]` instead.

              Filter by active binding status. When `true`, returns only policy sets with an
              active binding. When `false`, returns only policy sets without one. Omit to
              return all.

              Still honored for backward compatibility. Supplying both `active` and
              `filter[active]` with conflicting values returns `400 Bad Request`.

          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: **Deprecated.** Use `expand[]` instead.

              Opt-in to additional response fields. Still honored for backward compatibility;
              supplying both `expand` and `expand[]` with disagreeing values returns
              `400 Bad Request`.

          filter_active: Filter by active binding status. When `true`, returns only policy sets with an
              active binding. When `false`, returns only policy sets without one. Omit to
              return all.

          filter_owner_type: Filter on `owner_type`. Repeatable; repeated instances OR across values (e.g.
              `?filter[owner_type]=platform&filter[owner_type]=customer` matches either). See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `platform`, `customer`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values (e.g.
              `?filter[owner_type]=platform,customer`) are rejected with a 400 pointing at the
              repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          filter_scope_type: Filter on `scope_type` (policy sets only). Repeatable; repeated instances OR
              across values. See `FilterValues` in the shared spec for the full wire
              convention.

              Allowed values: `zone`, `resource`, `user`, `session`. Unknown values return 400
              with the list of allowed values. Comma-separated single values are rejected with
              a 400 pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query: Case-insensitive substring search across all searchable fields of the resource.
              For policies that is `name` and `description`; for policy sets that is `name`.
              Repeatable; if multiple terms are supplied they are OR-ed.

          query_name: Case-insensitive substring search on `name`. Repeatable; if multiple terms are
              supplied they are OR-ed (any matching term returns the row).

          sort: Field to sort by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/zones/{zone_id}/policy-sets", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "before": before,
                        "expand": expand,
                        "filter_active": filter_active,
                        "filter_owner_type": filter_owner_type,
                        "filter_scope_type": filter_scope_type,
                        "limit": limit,
                        "order": order,
                        "query": query,
                        "query_name": query_name,
                        "sort": sort,
                    },
                    policy_set_list_params.PolicySetListParams,
                ),
            ),
            cast_to=PolicySetListResponse,
        )

    async def archive(
        self,
        policy_set_id: str,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetWithBinding:
        """
        Archive a policy set

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/zones/{zone_id}/policy-sets/{policy_set_id}", zone_id=zone_id, policy_set_id=policy_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetWithBinding,
        )


class PolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_raw_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = to_raw_response_wrapper(
            policy_sets.list,
        )
        self.archive = to_raw_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Immutable policy set manifest snapshots"""
        return VersionsResourceWithRawResponse(self._policy_sets.versions)


class AsyncPolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_raw_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_raw_response_wrapper(
            policy_sets.list,
        )
        self.archive = async_to_raw_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResourceWithRawResponse(self._policy_sets.versions)


class PolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.archive = to_streamed_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Immutable policy set manifest snapshots"""
        return VersionsResourceWithStreamingResponse(self._policy_sets.versions)


class AsyncPolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            policy_sets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            policy_sets.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Immutable policy set manifest snapshots"""
        return AsyncVersionsResourceWithStreamingResponse(self._policy_sets.versions)
