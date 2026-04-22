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
from ....types.zones import policy_list_params, policy_create_params, policy_update_params
from ...._base_client import make_request_options
from ....types.zones.policy import Policy
from ....types.zones.policy_list_response import PolicyListResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    """Policy CRUD operations"""

    @cached_property
    def versions(self) -> VersionsResource:
        """Immutable policy version snapshots"""
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Create a new policy

        Args:
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
            path_template("/zones/{zone_id}/policies", zone_id=zone_id),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def retrieve(
        self,
        policy_id: str,
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
    ) -> Policy:
        """
        Get a policy by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
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
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def update(
        self,
        policy_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
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
    ) -> Policy:
        """
        Update a policy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
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
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_owner_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query: SequenceNotStr[str] | Omit = omit,
        query_description: SequenceNotStr[str] | Omit = omit,
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
    ) -> PolicyListResponse:
        """List policies in a zone

        Args:
          after: Cursor for forward pagination.

        Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: **Deprecated.** Use `expand[]` instead.

              Opt-in to additional response fields. Still honored for backward compatibility;
              supplying both `expand` and `expand[]` with disagreeing values returns
              `400 Bad Request`.

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

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query: Case-insensitive substring search across all searchable fields of the resource.
              For policies that is `name` and `description`; for policy sets that is `name`.
              Repeatable; if multiple terms are supplied they are OR-ed.

          query_description: Case-insensitive substring search on `description` (policies only). Repeatable;
              if multiple terms are supplied they are OR-ed.

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
            path_template("/zones/{zone_id}/policies", zone_id=zone_id),
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
                        "filter_owner_type": filter_owner_type,
                        "limit": limit,
                        "order": order,
                        "query": query,
                        "query_description": query_description,
                        "query_name": query_name,
                        "sort": sort,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            cast_to=PolicyListResponse,
        )

    def archive(
        self,
        policy_id: str,
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
    ) -> Policy:
        """
        Archive a policy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    """Policy CRUD operations"""

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Immutable policy version snapshots"""
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Create a new policy

        Args:
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
            path_template("/zones/{zone_id}/policies", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def retrieve(
        self,
        policy_id: str,
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
    ) -> Policy:
        """
        Get a policy by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
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
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def update(
        self,
        policy_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
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
    ) -> Policy:
        """
        Update a policy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
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
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_owner_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query: SequenceNotStr[str] | Omit = omit,
        query_description: SequenceNotStr[str] | Omit = omit,
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
    ) -> PolicyListResponse:
        """List policies in a zone

        Args:
          after: Cursor for forward pagination.

        Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: **Deprecated.** Use `expand[]` instead.

              Opt-in to additional response fields. Still honored for backward compatibility;
              supplying both `expand` and `expand[]` with disagreeing values returns
              `400 Bad Request`.

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

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query: Case-insensitive substring search across all searchable fields of the resource.
              For policies that is `name` and `description`; for policy sets that is `name`.
              Repeatable; if multiple terms are supplied they are OR-ed.

          query_description: Case-insensitive substring search on `description` (policies only). Repeatable;
              if multiple terms are supplied they are OR-ed.

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
            path_template("/zones/{zone_id}/policies", zone_id=zone_id),
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
                        "filter_owner_type": filter_owner_type,
                        "limit": limit,
                        "order": order,
                        "query": query,
                        "query_description": query_description,
                        "query_name": query_name,
                        "sort": sort,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            cast_to=PolicyListResponse,
        )

    async def archive(
        self,
        policy_id: str,
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
    ) -> Policy:
        """
        Archive a policy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/zones/{zone_id}/policies/{policy_id}", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.archive = to_raw_response_wrapper(
            policies.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Immutable policy version snapshots"""
        return VersionsResourceWithRawResponse(self._policies.versions)


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.archive = async_to_raw_response_wrapper(
            policies.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Immutable policy version snapshots"""
        return AsyncVersionsResourceWithRawResponse(self._policies.versions)


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.archive = to_streamed_response_wrapper(
            policies.archive,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Immutable policy version snapshots"""
        return VersionsResourceWithStreamingResponse(self._policies.versions)


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            policies.archive,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Immutable policy version snapshots"""
        return AsyncVersionsResourceWithStreamingResponse(self._policies.versions)
