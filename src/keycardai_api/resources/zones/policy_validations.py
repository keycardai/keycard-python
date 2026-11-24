# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import policy_validation_create_params
from ..._base_client import make_request_options
from ...types.zones.policy_validation_create_response import PolicyValidationCreateResponse

__all__ = ["PolicyValidationsResource", "AsyncPolicyValidationsResource"]


class PolicyValidationsResource(SyncAPIResource):
    """Stateless Cedar policy validation"""

    @cached_property
    def with_raw_response(self) -> PolicyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicyValidationsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        schema_version: str,
        cedar_json: Optional[object] | Omit = omit,
        cedar_raw: Optional[str] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyValidationCreateResponse:
        """
        Validate Cedar policy content against a schema

        Args:
          schema_version: Schema version to validate against. Must not be archived.

          cedar_json: Cedar policy in JSON representation. Mutually exclusive with cedar_raw.

          cedar_raw: Cedar policy in human-readable Cedar syntax. Mutually exclusive with cedar_json.

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
            path_template("/zones/{zone_id}/policy-validations", zone_id=zone_id),
            body=maybe_transform(
                {
                    "schema_version": schema_version,
                    "cedar_json": cedar_json,
                    "cedar_raw": cedar_raw,
                },
                policy_validation_create_params.PolicyValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyValidationCreateResponse,
        )


class AsyncPolicyValidationsResource(AsyncAPIResource):
    """Stateless Cedar policy validation"""

    @cached_property
    def with_raw_response(self) -> AsyncPolicyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicyValidationsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        schema_version: str,
        cedar_json: Optional[object] | Omit = omit,
        cedar_raw: Optional[str] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyValidationCreateResponse:
        """
        Validate Cedar policy content against a schema

        Args:
          schema_version: Schema version to validate against. Must not be archived.

          cedar_json: Cedar policy in JSON representation. Mutually exclusive with cedar_raw.

          cedar_raw: Cedar policy in human-readable Cedar syntax. Mutually exclusive with cedar_json.

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
            path_template("/zones/{zone_id}/policy-validations", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "schema_version": schema_version,
                    "cedar_json": cedar_json,
                    "cedar_raw": cedar_raw,
                },
                policy_validation_create_params.PolicyValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyValidationCreateResponse,
        )


class PolicyValidationsResourceWithRawResponse:
    def __init__(self, policy_validations: PolicyValidationsResource) -> None:
        self._policy_validations = policy_validations

        self.create = to_raw_response_wrapper(
            policy_validations.create,
        )


class AsyncPolicyValidationsResourceWithRawResponse:
    def __init__(self, policy_validations: AsyncPolicyValidationsResource) -> None:
        self._policy_validations = policy_validations

        self.create = async_to_raw_response_wrapper(
            policy_validations.create,
        )


class PolicyValidationsResourceWithStreamingResponse:
    def __init__(self, policy_validations: PolicyValidationsResource) -> None:
        self._policy_validations = policy_validations

        self.create = to_streamed_response_wrapper(
            policy_validations.create,
        )


class AsyncPolicyValidationsResourceWithStreamingResponse:
    def __init__(self, policy_validations: AsyncPolicyValidationsResource) -> None:
        self._policy_validations = policy_validations

        self.create = async_to_streamed_response_wrapper(
            policy_validations.create,
        )
