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
from ...types.zones import provider_list_params, provider_create_params, provider_update_params
from ..._base_client import make_request_options
from ...types.zones.provider import Provider
from ...types.zones.provider_list_response import ProviderListResponse

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: object | Omit = omit,
        protocols: provider_create_params.Protocols | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Creates a new Provider - a system that supplies access to Resources and allows
        actors to authenticate

        Args:
          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          client_id: OAuth 2.0 client identifier

          client_secret: OAuth 2.0 client secret (will be encrypted and stored securely)

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          metadata: Provider metadata

          protocols: Protocol-specific configuration for provider creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/providers", zone_id=zone_id),
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "description": description,
                    "metadata": metadata,
                    "protocols": protocols,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Returns details of a specific Provider by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def update(
        self,
        id: str,
        *,
        zone_id: str,
        client_id: Optional[str] | Omit = omit,
        client_secret: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[provider_update_params.Protocols] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Updates a Provider's configuration and metadata

        Args:
          client_id: OAuth 2.0 client identifier. Set to null to remove.

          client_secret: OAuth 2.0 client secret (will be encrypted and stored securely). Set to null to
              remove.

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          metadata: Provider metadata. Set to null to remove all metadata.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          protocols: Protocol-specific configuration. Set to null to remove all protocols.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "protocols": protocols,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        cursor: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        type: Literal["external", "keycard-vault", "keycard-sts"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Returns a list of providers in the specified zone

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
        return self._get(
            path_template("/zones/{zone_id}/providers", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "expand": expand,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                        "type": type,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: object | Omit = omit,
        protocols: provider_create_params.Protocols | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Creates a new Provider - a system that supplies access to Resources and allows
        actors to authenticate

        Args:
          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          client_id: OAuth 2.0 client identifier

          client_secret: OAuth 2.0 client secret (will be encrypted and stored securely)

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          metadata: Provider metadata

          protocols: Protocol-specific configuration for provider creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/providers", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "description": description,
                    "metadata": metadata,
                    "protocols": protocols,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Returns details of a specific Provider by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        client_id: Optional[str] | Omit = omit,
        client_secret: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[provider_update_params.Protocols] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Updates a Provider's configuration and metadata

        Args:
          client_id: OAuth 2.0 client identifier. Set to null to remove.

          client_secret: OAuth 2.0 client secret (will be encrypted and stored securely). Set to null to
              remove.

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          metadata: Provider metadata. Set to null to remove all metadata.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          protocols: Protocol-specific configuration. Set to null to remove all protocols.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "protocols": protocols,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        cursor: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        type: Literal["external", "keycard-vault", "keycard-sts"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Returns a list of providers in the specified zone

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
        return await self._get(
            path_template("/zones/{zone_id}/providers", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "expand": expand,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                        "type": type,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/zones/{zone_id}/providers/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_raw_response_wrapper(
            providers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            providers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            providers.update,
        )
        self.list = to_raw_response_wrapper(
            providers.list,
        )
        self.delete = to_raw_response_wrapper(
            providers.delete,
        )


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_raw_response_wrapper(
            providers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            providers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            providers.delete,
        )


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_streamed_response_wrapper(
            providers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            providers.update,
        )
        self.list = to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            providers.delete,
        )


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_streamed_response_wrapper(
            providers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            providers.delete,
        )
