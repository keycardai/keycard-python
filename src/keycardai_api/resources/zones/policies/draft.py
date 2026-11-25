# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zones.policies import draft_upsert_params, draft_retrieve_params
from ....types.zones.policy_draft import PolicyDraft

__all__ = ["DraftResource", "AsyncDraftResource"]


class DraftResource(SyncAPIResource):
    """Mutable policy authoring workspace"""

    @cached_property
    def with_raw_response(self) -> DraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return DraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return DraftResourceWithStreamingResponse(self)

    def retrieve(
        self,
        policy_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["user"], List[Literal["user"]]] | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDraft:
        """
        Get the draft for a policy

        Args:
          expand: Opt-in to additional response fields on a single resource (`user`). Repeatable.

          format: Narrows which Cedar representation the response includes. When omitted, both
              `cedar_json` and `cedar_raw` are populated. Pass `json` to receive only
              `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that don't care
              about payload size can skip this parameter.

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
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "format": format,
                    },
                    draft_retrieve_params.DraftRetrieveParams,
                ),
            ),
            cast_to=PolicyDraft,
        )

    def delete(
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
    ) -> None:
        """
        Delete a policy draft

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
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        policy_id: str,
        *,
        zone_id: str,
        schema_version: str,
        format: Literal["cedar", "json"] | Omit = omit,
        validate_cedar: bool | Omit = omit,
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
    ) -> PolicyDraft:
        """Create or update a policy draft

        Args:
          format: Response format override.

        `json` returns cedar_json, `cedar` returns cedar_raw.
              When omitted, the response matches the input format.

          validate_cedar: Whether to validate cedar_json against the schema. Defaults to true.

          cedar_json: Cedar policy in JSON representation. Mutually exclusive with cedar_raw.

          cedar_raw: Cedar policy in human-readable Cedar syntax. Mutually exclusive with cedar_json.

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
        return self._put(
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            body=maybe_transform(
                {
                    "schema_version": schema_version,
                    "cedar_json": cedar_json,
                    "cedar_raw": cedar_raw,
                },
                draft_upsert_params.DraftUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "validate_cedar": validate_cedar,
                    },
                    draft_upsert_params.DraftUpsertParams,
                ),
            ),
            cast_to=PolicyDraft,
        )


class AsyncDraftResource(AsyncAPIResource):
    """Mutable policy authoring workspace"""

    @cached_property
    def with_raw_response(self) -> AsyncDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncDraftResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        policy_id: str,
        *,
        zone_id: str,
        expand: Union[Literal["user"], List[Literal["user"]]] | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDraft:
        """
        Get the draft for a policy

        Args:
          expand: Opt-in to additional response fields on a single resource (`user`). Repeatable.

          format: Narrows which Cedar representation the response includes. When omitted, both
              `cedar_json` and `cedar_raw` are populated. Pass `json` to receive only
              `cedar_json`, or `cedar` to receive only `cedar_raw`. Callers that don't care
              about payload size can skip this parameter.

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
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "format": format,
                    },
                    draft_retrieve_params.DraftRetrieveParams,
                ),
            ),
            cast_to=PolicyDraft,
        )

    async def delete(
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
    ) -> None:
        """
        Delete a policy draft

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
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        policy_id: str,
        *,
        zone_id: str,
        schema_version: str,
        format: Literal["cedar", "json"] | Omit = omit,
        validate_cedar: bool | Omit = omit,
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
    ) -> PolicyDraft:
        """Create or update a policy draft

        Args:
          format: Response format override.

        `json` returns cedar_json, `cedar` returns cedar_raw.
              When omitted, the response matches the input format.

          validate_cedar: Whether to validate cedar_json against the schema. Defaults to true.

          cedar_json: Cedar policy in JSON representation. Mutually exclusive with cedar_raw.

          cedar_raw: Cedar policy in human-readable Cedar syntax. Mutually exclusive with cedar_json.

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
        return await self._put(
            path_template("/zones/{zone_id}/policies/{policy_id}/draft", zone_id=zone_id, policy_id=policy_id),
            body=await async_maybe_transform(
                {
                    "schema_version": schema_version,
                    "cedar_json": cedar_json,
                    "cedar_raw": cedar_raw,
                },
                draft_upsert_params.DraftUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "validate_cedar": validate_cedar,
                    },
                    draft_upsert_params.DraftUpsertParams,
                ),
            ),
            cast_to=PolicyDraft,
        )


class DraftResourceWithRawResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.retrieve = to_raw_response_wrapper(
            draft.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            draft.delete,
        )
        self.upsert = to_raw_response_wrapper(
            draft.upsert,
        )


class AsyncDraftResourceWithRawResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.retrieve = async_to_raw_response_wrapper(
            draft.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            draft.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            draft.upsert,
        )


class DraftResourceWithStreamingResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.retrieve = to_streamed_response_wrapper(
            draft.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            draft.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            draft.upsert,
        )


class AsyncDraftResourceWithStreamingResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.retrieve = async_to_streamed_response_wrapper(
            draft.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            draft.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            draft.upsert,
        )
