# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import policy_binding_set_params, policy_binding_list_params, policy_binding_retrieve_metrics_params
from ..._base_client import make_request_options
from ...types.zones.policy_set_binding import PolicySetBinding
from ...types.zones.policy_binding_list_response import PolicyBindingListResponse
from ...types.zones.policy_binding_retrieve_metrics_response import PolicyBindingRetrieveMetricsResponse

__all__ = ["PolicyBindingsResource", "AsyncPolicyBindingsResource"]


class PolicyBindingsResource(SyncAPIResource):
    """Policy set binding management.

    Active slots are replace-only by design:
    once bound (at zone bootstrap or on a principal's first policy check), an
    active slot is never emptied — evaluation fails closed, so an empty active
    slot would deny all access. Replace the bound version rather than removing
    the binding. DELETE applies to shadow bindings only.
    """

    @cached_property
    def with_raw_response(self) -> PolicyBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicyBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicyBindingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        binding_id: str,
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
    ) -> PolicySetBinding:
        """
        Returns a specific binding by its stable identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
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
            path_template("/zones/{zone_id}/policy-bindings/{binding_id}", zone_id=zone_id, binding_id=binding_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetBinding,
        )

    def list(
        self,
        zone_id: str,
        *,
        filter_mode: SequenceNotStr[str] | Omit = omit,
        filter_target_id: SequenceNotStr[str] | Omit = omit,
        filter_target_type: SequenceNotStr[str] | Omit = omit,
        mode: Literal["shadow"] | Omit = omit,
        scope_type: Literal["zone"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyBindingListResponse:
        """
        Returns bindings for the zone, filtered by target and mode.

        `filter[target_type]` defaults to `zone` and `filter[mode]` defaults to `shadow`
        when omitted (preserving the endpoint's historical shadow-only listing); pass
        explicit values to widen. The deprecated bare `scope_type` and `mode` parameters
        are honored as equivalents and suppress the respective defaults; supplying a
        bare parameter and its `filter[...]` form with different values returns 400.
        With an effective target type set of exactly `zone`, `filter[target_id]` values
        other than the zone ID return 400.

        Args:
          filter_mode: Filter on binding `mode`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `active`, `shadow`. Unknown values return 400 with the list of
              allowed values. Comma-separated single values are rejected with a 400 pointing
              at the repeated-parameter OR form.

              **Defaults to `shadow`** when omitted (and the deprecated bare `mode` parameter
              is absent), preserving the endpoint's historical shadow-only listing. Pass
              `filter[mode]=active` (or both values) to widen.

          filter_target_id: Filter on `target_id`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Zone-targeted elements carry the zone ID as their `target_id`. When the
              effective `filter[target_type]` set is exactly `zone` (including via its
              default), any `filter[target_id]` value other than the path `zone_id` returns
              `400 Bad Request`.

          filter_target_type: Filter on `target_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `zone`, `user` (`resource` and `session` are reserved and not
              yet accepted). Unknown values return 400 with the list of allowed values.
              Comma-separated single values are rejected with a 400 pointing at the
              repeated-parameter OR form.

              **Defaults to `zone`** when omitted (and no deprecated equivalent parameter is
              supplied), so listings exclude principal-scoped elements unless explicitly
              widened. On `listPolicies` the default is skipped when `filter[id]` is present,
              so by-ID fetches resolve regardless of target.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          mode: **Deprecated.** Use `filter[mode]` instead. Still honored for backward
              compatibility but only accepts `shadow`; other values return 400. Conflicts with
              `filter[mode]` return 400.

          scope_type: **Deprecated.** Use `filter[target_type]` instead. Still honored for backward
              compatibility but only accepts `zone`; other values return 400. Conflicts with
              `filter[target_type]` return 400.

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
            path_template("/zones/{zone_id}/policy-bindings", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_mode": filter_mode,
                        "filter_target_id": filter_target_id,
                        "filter_target_type": filter_target_type,
                        "mode": mode,
                        "scope_type": scope_type,
                    },
                    policy_binding_list_params.PolicyBindingListParams,
                ),
            ),
            cast_to=PolicyBindingListResponse,
        )

    def delete(
        self,
        binding_id: str,
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
    ) -> None:
        """
        Removes a binding by its identifier, stopping evaluation for that slot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            path_template("/zones/{zone_id}/policy-bindings/{binding_id}", zone_id=zone_id, binding_id=binding_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_metrics(
        self,
        binding_id: str,
        *,
        zone_id: str,
        policy_set_id: str | Omit = omit,
        psv_id: str | Omit = omit,
        scope: Literal["binding", "zone"] | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyBindingRetrieveMetricsResponse:
        """Returns shadow evaluation metrics for a specific binding.

        Use query parameters
        to change scope:

        - `scope=zone` — zone-level aggregate across all pairings
        - `psv_id=<id>` — metrics for a specific policy set version (in any role),
          including per-pairing breakdown

        Args:
          policy_set_id: Policy set to filter metrics for. Required when psv_id is provided.

          psv_id: Filter to a specific policy set version (in any role). When provided, response
              includes per-pairing breakdown. Requires policy_set_id.

          scope: Metrics scope. `binding` (default) returns metrics for this binding. `zone`
              returns zone-level aggregate across all pairings.

          since: Start of the time window (default 24h ago)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
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
            path_template(
                "/zones/{zone_id}/policy-bindings/{binding_id}/metrics", zone_id=zone_id, binding_id=binding_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "policy_set_id": policy_set_id,
                        "psv_id": psv_id,
                        "scope": scope,
                        "since": since,
                    },
                    policy_binding_retrieve_metrics_params.PolicyBindingRetrieveMetricsParams,
                ),
            ),
            cast_to=PolicyBindingRetrieveMetricsResponse,
        )

    def set(
        self,
        zone_id: str,
        *,
        mode: Literal["shadow"],
        policy_set_id: str,
        policy_set_version_id: str,
        scope_target_id: str | Omit = omit,
        scope_type: Literal["zone"] | Omit = omit,
        target_id: str | Omit = omit,
        target_type: Literal["zone"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetBinding:
        """
        Upserts a binding for a slot identified by (scope_type, scope_target_id, mode).
        If a binding already exists for the slot, it is replaced. The binding ID is
        stable per slot and survives replacements.

        Args:
          mode: Binding mode

          policy_set_id: Public ID of the policy set to bind

          policy_set_version_id: Public ID of the policy set version to bind

          scope_target_id: **Deprecated.** Use `target_id` instead.

          scope_type: **Deprecated.** Use `target_type` instead.

          target_id: Defaults to zone_id for zone targets. Required for other targets.

          target_type: What the binding targets. Only `zone` is supported for direct binding writes.

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
        return self._put(
            path_template("/zones/{zone_id}/policy-bindings", zone_id=zone_id),
            body=maybe_transform(
                {
                    "mode": mode,
                    "policy_set_id": policy_set_id,
                    "policy_set_version_id": policy_set_version_id,
                    "scope_target_id": scope_target_id,
                    "scope_type": scope_type,
                    "target_id": target_id,
                    "target_type": target_type,
                },
                policy_binding_set_params.PolicyBindingSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetBinding,
        )


class AsyncPolicyBindingsResource(AsyncAPIResource):
    """Policy set binding management.

    Active slots are replace-only by design:
    once bound (at zone bootstrap or on a principal's first policy check), an
    active slot is never emptied — evaluation fails closed, so an empty active
    slot would deny all access. Replace the bound version rather than removing
    the binding. DELETE applies to shadow bindings only.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPolicyBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicyBindingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        binding_id: str,
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
    ) -> PolicySetBinding:
        """
        Returns a specific binding by its stable identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
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
            path_template("/zones/{zone_id}/policy-bindings/{binding_id}", zone_id=zone_id, binding_id=binding_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetBinding,
        )

    async def list(
        self,
        zone_id: str,
        *,
        filter_mode: SequenceNotStr[str] | Omit = omit,
        filter_target_id: SequenceNotStr[str] | Omit = omit,
        filter_target_type: SequenceNotStr[str] | Omit = omit,
        mode: Literal["shadow"] | Omit = omit,
        scope_type: Literal["zone"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyBindingListResponse:
        """
        Returns bindings for the zone, filtered by target and mode.

        `filter[target_type]` defaults to `zone` and `filter[mode]` defaults to `shadow`
        when omitted (preserving the endpoint's historical shadow-only listing); pass
        explicit values to widen. The deprecated bare `scope_type` and `mode` parameters
        are honored as equivalents and suppress the respective defaults; supplying a
        bare parameter and its `filter[...]` form with different values returns 400.
        With an effective target type set of exactly `zone`, `filter[target_id]` values
        other than the zone ID return 400.

        Args:
          filter_mode: Filter on binding `mode`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `active`, `shadow`. Unknown values return 400 with the list of
              allowed values. Comma-separated single values are rejected with a 400 pointing
              at the repeated-parameter OR form.

              **Defaults to `shadow`** when omitted (and the deprecated bare `mode` parameter
              is absent), preserving the endpoint's historical shadow-only listing. Pass
              `filter[mode]=active` (or both values) to widen.

          filter_target_id: Filter on `target_id`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Zone-targeted elements carry the zone ID as their `target_id`. When the
              effective `filter[target_type]` set is exactly `zone` (including via its
              default), any `filter[target_id]` value other than the path `zone_id` returns
              `400 Bad Request`.

          filter_target_type: Filter on `target_type`. Repeatable; repeated instances OR across values. See
              `FilterValues` in the shared spec for the full wire convention.

              Allowed values: `zone`, `user` (`resource` and `session` are reserved and not
              yet accepted). Unknown values return 400 with the list of allowed values.
              Comma-separated single values are rejected with a 400 pointing at the
              repeated-parameter OR form.

              **Defaults to `zone`** when omitted (and no deprecated equivalent parameter is
              supplied), so listings exclude principal-scoped elements unless explicitly
              widened. On `listPolicies` the default is skipped when `filter[id]` is present,
              so by-ID fetches resolve regardless of target.

              Note: the allowed-value enum is enforced in the handler (not as an OpenAPI
              `items.enum`) so the server can return a targeted error for the comma-AND form
              instead of a generic "not in allowed values" response.

          mode: **Deprecated.** Use `filter[mode]` instead. Still honored for backward
              compatibility but only accepts `shadow`; other values return 400. Conflicts with
              `filter[mode]` return 400.

          scope_type: **Deprecated.** Use `filter[target_type]` instead. Still honored for backward
              compatibility but only accepts `zone`; other values return 400. Conflicts with
              `filter[target_type]` return 400.

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
            path_template("/zones/{zone_id}/policy-bindings", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_mode": filter_mode,
                        "filter_target_id": filter_target_id,
                        "filter_target_type": filter_target_type,
                        "mode": mode,
                        "scope_type": scope_type,
                    },
                    policy_binding_list_params.PolicyBindingListParams,
                ),
            ),
            cast_to=PolicyBindingListResponse,
        )

    async def delete(
        self,
        binding_id: str,
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
    ) -> None:
        """
        Removes a binding by its identifier, stopping evaluation for that slot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            path_template("/zones/{zone_id}/policy-bindings/{binding_id}", zone_id=zone_id, binding_id=binding_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_metrics(
        self,
        binding_id: str,
        *,
        zone_id: str,
        policy_set_id: str | Omit = omit,
        psv_id: str | Omit = omit,
        scope: Literal["binding", "zone"] | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyBindingRetrieveMetricsResponse:
        """Returns shadow evaluation metrics for a specific binding.

        Use query parameters
        to change scope:

        - `scope=zone` — zone-level aggregate across all pairings
        - `psv_id=<id>` — metrics for a specific policy set version (in any role),
          including per-pairing breakdown

        Args:
          policy_set_id: Policy set to filter metrics for. Required when psv_id is provided.

          psv_id: Filter to a specific policy set version (in any role). When provided, response
              includes per-pairing breakdown. Requires policy_set_id.

          scope: Metrics scope. `binding` (default) returns metrics for this binding. `zone`
              returns zone-level aggregate across all pairings.

          since: Start of the time window (default 24h ago)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
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
            path_template(
                "/zones/{zone_id}/policy-bindings/{binding_id}/metrics", zone_id=zone_id, binding_id=binding_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "policy_set_id": policy_set_id,
                        "psv_id": psv_id,
                        "scope": scope,
                        "since": since,
                    },
                    policy_binding_retrieve_metrics_params.PolicyBindingRetrieveMetricsParams,
                ),
            ),
            cast_to=PolicyBindingRetrieveMetricsResponse,
        )

    async def set(
        self,
        zone_id: str,
        *,
        mode: Literal["shadow"],
        policy_set_id: str,
        policy_set_version_id: str,
        scope_target_id: str | Omit = omit,
        scope_type: Literal["zone"] | Omit = omit,
        target_id: str | Omit = omit,
        target_type: Literal["zone"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetBinding:
        """
        Upserts a binding for a slot identified by (scope_type, scope_target_id, mode).
        If a binding already exists for the slot, it is replaced. The binding ID is
        stable per slot and survives replacements.

        Args:
          mode: Binding mode

          policy_set_id: Public ID of the policy set to bind

          policy_set_version_id: Public ID of the policy set version to bind

          scope_target_id: **Deprecated.** Use `target_id` instead.

          scope_type: **Deprecated.** Use `target_type` instead.

          target_id: Defaults to zone_id for zone targets. Required for other targets.

          target_type: What the binding targets. Only `zone` is supported for direct binding writes.

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
        return await self._put(
            path_template("/zones/{zone_id}/policy-bindings", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "policy_set_id": policy_set_id,
                    "policy_set_version_id": policy_set_version_id,
                    "scope_target_id": scope_target_id,
                    "scope_type": scope_type,
                    "target_id": target_id,
                    "target_type": target_type,
                },
                policy_binding_set_params.PolicyBindingSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicySetBinding,
        )


class PolicyBindingsResourceWithRawResponse:
    def __init__(self, policy_bindings: PolicyBindingsResource) -> None:
        self._policy_bindings = policy_bindings

        self.retrieve = to_raw_response_wrapper(
            policy_bindings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            policy_bindings.list,
        )
        self.delete = to_raw_response_wrapper(
            policy_bindings.delete,
        )
        self.retrieve_metrics = to_raw_response_wrapper(
            policy_bindings.retrieve_metrics,
        )
        self.set = to_raw_response_wrapper(
            policy_bindings.set,
        )


class AsyncPolicyBindingsResourceWithRawResponse:
    def __init__(self, policy_bindings: AsyncPolicyBindingsResource) -> None:
        self._policy_bindings = policy_bindings

        self.retrieve = async_to_raw_response_wrapper(
            policy_bindings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            policy_bindings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policy_bindings.delete,
        )
        self.retrieve_metrics = async_to_raw_response_wrapper(
            policy_bindings.retrieve_metrics,
        )
        self.set = async_to_raw_response_wrapper(
            policy_bindings.set,
        )


class PolicyBindingsResourceWithStreamingResponse:
    def __init__(self, policy_bindings: PolicyBindingsResource) -> None:
        self._policy_bindings = policy_bindings

        self.retrieve = to_streamed_response_wrapper(
            policy_bindings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            policy_bindings.list,
        )
        self.delete = to_streamed_response_wrapper(
            policy_bindings.delete,
        )
        self.retrieve_metrics = to_streamed_response_wrapper(
            policy_bindings.retrieve_metrics,
        )
        self.set = to_streamed_response_wrapper(
            policy_bindings.set,
        )


class AsyncPolicyBindingsResourceWithStreamingResponse:
    def __init__(self, policy_bindings: AsyncPolicyBindingsResource) -> None:
        self._policy_bindings = policy_bindings

        self.retrieve = async_to_streamed_response_wrapper(
            policy_bindings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_bindings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policy_bindings.delete,
        )
        self.retrieve_metrics = async_to_streamed_response_wrapper(
            policy_bindings.retrieve_metrics,
        )
        self.set = async_to_streamed_response_wrapper(
            policy_bindings.set,
        )
