# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import policy_evaluation_create_params, policy_evaluation_list_requests_params
from ..._base_client import make_request_options
from ...types.zones.policy_evaluation_create_response import PolicyEvaluationCreateResponse
from ...types.zones.policy_evaluation_list_requests_response import PolicyEvaluationListRequestsResponse

__all__ = ["PolicyEvaluationsResource", "AsyncPolicyEvaluationsResource"]


class PolicyEvaluationsResource(SyncAPIResource):
    """Stateless policy evaluation testing"""

    @cached_property
    def with_raw_response(self) -> PolicyEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicyEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicyEvaluationsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        action: str,
        policy_source: policy_evaluation_create_params.PolicySource,
        principal_id: str,
        principal_type: Literal["user", "application"],
        resource_id: str,
        acting_principal_id: str | Omit = omit,
        authority_type: Optional[Literal["delegation", "impersonation"]] | Omit = omit,
        context: policy_evaluation_create_params.Context | Omit = omit,
        subject_id: str | Omit = omit,
        subject_type: Literal["user", "application"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyEvaluationCreateResponse:
        """
        Stateless evaluation endpoint for testing Cedar policy evaluation against real
        entities before deployment. Supports evaluating a single policy, a full policy
        set, or raw Cedar text.

        Args:
          action: Cedar action to evaluate (e.g. `any`). The engine namespaces actions
              automatically as `Keycard::Action::"<name>"`.

          policy_source: Specifies which policies to evaluate. Exactly one of policy, policy_set, raw, or
              manifest must be provided.

          principal_id: Public ID of the user or application.

          resource_id: Public ID of the resource.

          acting_principal_id: ID of the acting application from a verified RFC 8693 `actor_token`, as sent on
              `/policy/check`. Resolved with the same entity lookup as an application
              `principal_id` and exposed to Cedar as `context.acting_principal.application` on
              both checks. Lets a captured evaluation request be replayed faithfully.

          authority_type: Discriminator for the subject authority model. Determines how the subject
              relationship is expressed in the Cedar context:

              - `"delegation"` — sets `context.on_behalf = true` on the actor check. The actor
                is acting on behalf of the subject.
              - `"impersonation"` — sets `context.impersonate = true` on the actor check. The
                actor is impersonating the subject. When null and a subject is present,
                defaults to `"delegation"` for backward compatibility.

          context: Additional context for Cedar authorization evaluation. Fields here are mapped
              directly into the Cedar `context` record.

          subject_id: Public ID of the subject (required when subject_type is set).

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
            path_template("/zones/{zone_id}/policy-evaluations", zone_id=zone_id),
            body=maybe_transform(
                {
                    "action": action,
                    "policy_source": policy_source,
                    "principal_id": principal_id,
                    "principal_type": principal_type,
                    "resource_id": resource_id,
                    "acting_principal_id": acting_principal_id,
                    "authority_type": authority_type,
                    "context": context,
                    "subject_id": subject_id,
                    "subject_type": subject_type,
                },
                policy_evaluation_create_params.PolicyEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyEvaluationCreateResponse,
        )

    def list_requests(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        filter_active_decision: SequenceNotStr[str] | Omit = omit,
        filter_authority_type: SequenceNotStr[str] | Omit = omit,
        filter_has_shadow: bool | Omit = omit,
        filter_principal_id: SequenceNotStr[str] | Omit = omit,
        filter_principal_type: SequenceNotStr[str] | Omit = omit,
        filter_resource_id: SequenceNotStr[str] | Omit = omit,
        filter_subject_id: SequenceNotStr[str] | Omit = omit,
        filter_subject_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query_action: SequenceNotStr[str] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyEvaluationListRequestsResponse:
        """
        Returns a paginated list of evaluation request entries captured from live
        credentials API traffic for the specified zone. Sorted by created_at descending
        (newest first). Use with the test evaluation endpoint for replay-based impact
        analysis.

        Args:
          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: Opt-in to additional response fields (`total_count`, `user`). Repeatable;
              matches the `expand[]` convention used across the Keycard API.

          filter_active_decision: Filter on `active_decision`. Repeatable; repeated instances OR across values.
              See `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `allow`, `deny`. Unknown values return 400 with the list of
              allowed values. Comma-separated single values are rejected with a 400 pointing
              at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          filter_authority_type: Filter on `authority_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention. Rows with `NULL`
              authority_type are excluded when this filter is present.

              Allowed values: `delegation`, `impersonation`. Unknown values return 400 with
              the list of allowed values. Comma-separated single values are rejected with a
              400 pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler.

          filter_has_shadow: Filter by shadow-evaluation presence. When `true`, returns only requests that
              had a shadow policy set version (`shadow_psv_id IS NOT NULL`). When `false`,
              returns only requests without one. Omit to return all.

          filter_principal_id: Filter on `principal_id` by exact match. Repeatable; repeated instances OR
              across values. See `FilterValues` in the shared spec for the full wire
              convention. Comma-separated single values are rejected with a 400 pointing at
              the repeated-parameter OR form.

          filter_principal_type: Filter on `principal_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `user`, `application`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values are rejected with a 400
              pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form.

          filter_resource_id: Filter on `resource_id` by exact match. Repeatable; repeated instances OR across
              values. See `FilterValues` in the shared spec for the full wire convention.
              Comma-separated single values are rejected with a 400 pointing at the
              repeated-parameter OR form.

          filter_subject_id: Filter on `subject_id` by exact match. Repeatable; repeated instances OR across
              values. Rows with `NULL` subject_id are excluded when this filter is present.
              See `FilterValues` in the shared spec for the full wire convention.

          filter_subject_type: Filter on `subject_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention. Rows with `NULL`
              subject_type are excluded when this filter is present.

              Allowed values: `user`, `application`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values are rejected with a 400
              pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query_action: Case-insensitive substring search on `action`. Repeatable; if multiple terms are
              supplied they are OR-ed.

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
            path_template("/zones/{zone_id}/policy-evaluations/requests", zone_id=zone_id),
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
                        "filter_active_decision": filter_active_decision,
                        "filter_authority_type": filter_authority_type,
                        "filter_has_shadow": filter_has_shadow,
                        "filter_principal_id": filter_principal_id,
                        "filter_principal_type": filter_principal_type,
                        "filter_resource_id": filter_resource_id,
                        "filter_subject_id": filter_subject_id,
                        "filter_subject_type": filter_subject_type,
                        "limit": limit,
                        "order": order,
                        "query_action": query_action,
                        "sort": sort,
                    },
                    policy_evaluation_list_requests_params.PolicyEvaluationListRequestsParams,
                ),
            ),
            cast_to=PolicyEvaluationListRequestsResponse,
        )


class AsyncPolicyEvaluationsResource(AsyncAPIResource):
    """Stateless policy evaluation testing"""

    @cached_property
    def with_raw_response(self) -> AsyncPolicyEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicyEvaluationsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        action: str,
        policy_source: policy_evaluation_create_params.PolicySource,
        principal_id: str,
        principal_type: Literal["user", "application"],
        resource_id: str,
        acting_principal_id: str | Omit = omit,
        authority_type: Optional[Literal["delegation", "impersonation"]] | Omit = omit,
        context: policy_evaluation_create_params.Context | Omit = omit,
        subject_id: str | Omit = omit,
        subject_type: Literal["user", "application"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyEvaluationCreateResponse:
        """
        Stateless evaluation endpoint for testing Cedar policy evaluation against real
        entities before deployment. Supports evaluating a single policy, a full policy
        set, or raw Cedar text.

        Args:
          action: Cedar action to evaluate (e.g. `any`). The engine namespaces actions
              automatically as `Keycard::Action::"<name>"`.

          policy_source: Specifies which policies to evaluate. Exactly one of policy, policy_set, raw, or
              manifest must be provided.

          principal_id: Public ID of the user or application.

          resource_id: Public ID of the resource.

          acting_principal_id: ID of the acting application from a verified RFC 8693 `actor_token`, as sent on
              `/policy/check`. Resolved with the same entity lookup as an application
              `principal_id` and exposed to Cedar as `context.acting_principal.application` on
              both checks. Lets a captured evaluation request be replayed faithfully.

          authority_type: Discriminator for the subject authority model. Determines how the subject
              relationship is expressed in the Cedar context:

              - `"delegation"` — sets `context.on_behalf = true` on the actor check. The actor
                is acting on behalf of the subject.
              - `"impersonation"` — sets `context.impersonate = true` on the actor check. The
                actor is impersonating the subject. When null and a subject is present,
                defaults to `"delegation"` for backward compatibility.

          context: Additional context for Cedar authorization evaluation. Fields here are mapped
              directly into the Cedar `context` record.

          subject_id: Public ID of the subject (required when subject_type is set).

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
            path_template("/zones/{zone_id}/policy-evaluations", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "policy_source": policy_source,
                    "principal_id": principal_id,
                    "principal_type": principal_type,
                    "resource_id": resource_id,
                    "acting_principal_id": acting_principal_id,
                    "authority_type": authority_type,
                    "context": context,
                    "subject_id": subject_id,
                    "subject_type": subject_type,
                },
                policy_evaluation_create_params.PolicyEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyEvaluationCreateResponse,
        )

    async def list_requests(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: Union[Literal["total_count", "user"], List[Literal["total_count", "user"]]] | Omit = omit,
        filter_active_decision: SequenceNotStr[str] | Omit = omit,
        filter_authority_type: SequenceNotStr[str] | Omit = omit,
        filter_has_shadow: bool | Omit = omit,
        filter_principal_id: SequenceNotStr[str] | Omit = omit,
        filter_principal_type: SequenceNotStr[str] | Omit = omit,
        filter_resource_id: SequenceNotStr[str] | Omit = omit,
        filter_subject_id: SequenceNotStr[str] | Omit = omit,
        filter_subject_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        query_action: SequenceNotStr[str] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyEvaluationListRequestsResponse:
        """
        Returns a paginated list of evaluation request entries captured from live
        credentials API traffic for the specified zone. Sorted by created_at descending
        (newest first). Use with the test evaluation endpoint for replay-based impact
        analysis.

        Args:
          after: Cursor for forward pagination. Returned in `Pagination.after_cursor`. Mutually
              exclusive with `before`.

          before: Cursor for backward pagination. Returned in `Pagination.before_cursor`. Mutually
              exclusive with `after`.

          expand: Opt-in to additional response fields (`total_count`, `user`). Repeatable;
              matches the `expand[]` convention used across the Keycard API.

          filter_active_decision: Filter on `active_decision`. Repeatable; repeated instances OR across values.
              See `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `allow`, `deny`. Unknown values return 400 with the list of
              allowed values. Comma-separated single values are rejected with a 400 pointing
              at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          filter_authority_type: Filter on `authority_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention. Rows with `NULL`
              authority_type are excluded when this filter is present.

              Allowed values: `delegation`, `impersonation`. Unknown values return 400 with
              the list of allowed values. Comma-separated single values are rejected with a
              400 pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler.

          filter_has_shadow: Filter by shadow-evaluation presence. When `true`, returns only requests that
              had a shadow policy set version (`shadow_psv_id IS NOT NULL`). When `false`,
              returns only requests without one. Omit to return all.

          filter_principal_id: Filter on `principal_id` by exact match. Repeatable; repeated instances OR
              across values. See `FilterValues` in the shared spec for the full wire
              convention. Comma-separated single values are rejected with a 400 pointing at
              the repeated-parameter OR form.

          filter_principal_type: Filter on `principal_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `user`, `application`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values are rejected with a 400
              pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form.

          filter_resource_id: Filter on `resource_id` by exact match. Repeatable; repeated instances OR across
              values. See `FilterValues` in the shared spec for the full wire convention.
              Comma-separated single values are rejected with a 400 pointing at the
              repeated-parameter OR form.

          filter_subject_id: Filter on `subject_id` by exact match. Repeatable; repeated instances OR across
              values. Rows with `NULL` subject_id are excluded when this filter is present.
              See `FilterValues` in the shared spec for the full wire convention.

          filter_subject_type: Filter on `subject_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention. Rows with `NULL`
              subject_type are excluded when this filter is present.

              Allowed values: `user`, `application`. Unknown values return 400 with the list
              of allowed values. Comma-separated single values are rejected with a 400
              pointing at the repeated-parameter OR form.

              Note: the allowed-value enum is enforced in the handler.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

          query_action: Case-insensitive substring search on `action`. Repeatable; if multiple terms are
              supplied they are OR-ed.

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
            path_template("/zones/{zone_id}/policy-evaluations/requests", zone_id=zone_id),
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
                        "filter_active_decision": filter_active_decision,
                        "filter_authority_type": filter_authority_type,
                        "filter_has_shadow": filter_has_shadow,
                        "filter_principal_id": filter_principal_id,
                        "filter_principal_type": filter_principal_type,
                        "filter_resource_id": filter_resource_id,
                        "filter_subject_id": filter_subject_id,
                        "filter_subject_type": filter_subject_type,
                        "limit": limit,
                        "order": order,
                        "query_action": query_action,
                        "sort": sort,
                    },
                    policy_evaluation_list_requests_params.PolicyEvaluationListRequestsParams,
                ),
            ),
            cast_to=PolicyEvaluationListRequestsResponse,
        )


class PolicyEvaluationsResourceWithRawResponse:
    def __init__(self, policy_evaluations: PolicyEvaluationsResource) -> None:
        self._policy_evaluations = policy_evaluations

        self.create = to_raw_response_wrapper(
            policy_evaluations.create,
        )
        self.list_requests = to_raw_response_wrapper(
            policy_evaluations.list_requests,
        )


class AsyncPolicyEvaluationsResourceWithRawResponse:
    def __init__(self, policy_evaluations: AsyncPolicyEvaluationsResource) -> None:
        self._policy_evaluations = policy_evaluations

        self.create = async_to_raw_response_wrapper(
            policy_evaluations.create,
        )
        self.list_requests = async_to_raw_response_wrapper(
            policy_evaluations.list_requests,
        )


class PolicyEvaluationsResourceWithStreamingResponse:
    def __init__(self, policy_evaluations: PolicyEvaluationsResource) -> None:
        self._policy_evaluations = policy_evaluations

        self.create = to_streamed_response_wrapper(
            policy_evaluations.create,
        )
        self.list_requests = to_streamed_response_wrapper(
            policy_evaluations.list_requests,
        )


class AsyncPolicyEvaluationsResourceWithStreamingResponse:
    def __init__(self, policy_evaluations: AsyncPolicyEvaluationsResource) -> None:
        self._policy_evaluations = policy_evaluations

        self.create = async_to_streamed_response_wrapper(
            policy_evaluations.create,
        )
        self.list_requests = async_to_streamed_response_wrapper(
            policy_evaluations.list_requests,
        )
