# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import (
    resource_list_params,
    resource_create_params,
    resource_update_params,
)
from ..._base_client import make_request_options
from ...types.zones.metadata_param import MetadataParam
from ...types.zones.applications.resource import Resource
from ...types.zones.metadata_update_param import MetadataUpdateParam
from ...types.zones.resource_list_response import ResourceListResponse

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        application_id: str | Omit = omit,
        application_type: Literal["native", "web"] | Omit = omit,
        credential_provider_id: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Creates a new Resource - a system that exposes protected information or
        functionality requiring authentication

        Args:
          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          application_id: ID of the application that provides this resource

          application_type: The expected type of client for this credential. Native clients must use
              localhost URLs for redirect_uris or URIs with custom schemes. Web clients must
              use https URLs and must not use localhost as the hostname.

          credential_provider_id: ID of the credential provider to associate with the resource

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          metadata: Entity metadata

          scopes: Scopes supported by the resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/resources", zone_id=zone_id),
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "application_id": application_id,
                    "application_type": application_type,
                    "credential_provider_id": credential_provider_id,
                    "description": description,
                    "metadata": metadata,
                    "scopes": scopes,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
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
    ) -> Resource:
        """
        Returns details of a specific Resource by ID

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    def update(
        self,
        id: str,
        *,
        zone_id: str,
        application_id: Optional[str] | Omit = omit,
        application_type: Literal["native", "web"] | Omit = omit,
        credential_provider_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[MetadataUpdateParam] | Omit = omit,
        name: str | Omit = omit,
        scopes: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Updates a Resource's configuration and metadata

        Args:
          application_id: ID of the application that provides this resource (set to null to unset)

          application_type: The expected type of client for this credential. Native clients must use
              localhost URLs for redirect_uris or URIs with custom schemes. Web clients must
              use https URLs and must not use localhost as the hostname.

          credential_provider_id: ID of the credential provider to associate with the resource (set to null to
              unset)

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          metadata: Entity metadata (set to null or {} to remove metadata)

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          scopes: Scopes supported by the resource (set to null to unset)

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            body=maybe_transform(
                {
                    "application_id": application_id,
                    "application_type": application_type,
                    "credential_provider_id": credential_provider_id,
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "scopes": scopes,
                },
                resource_update_params.ResourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        credential_provider_id: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceListResponse:
        """
        Returns a list of resources in the specified zone

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          credential_provider_id: Filter resources by credential provider ID

          identifier: Filter resources by identifier

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/resources", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "credential_provider_id": credential_provider_id,
                        "expand": expand,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            cast_to=ResourceListResponse,
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
        Permanently deletes a Resource

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        application_id: str | Omit = omit,
        application_type: Literal["native", "web"] | Omit = omit,
        credential_provider_id: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Creates a new Resource - a system that exposes protected information or
        functionality requiring authentication

        Args:
          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          application_id: ID of the application that provides this resource

          application_type: The expected type of client for this credential. Native clients must use
              localhost URLs for redirect_uris or URIs with custom schemes. Web clients must
              use https URLs and must not use localhost as the hostname.

          credential_provider_id: ID of the credential provider to associate with the resource

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          metadata: Entity metadata

          scopes: Scopes supported by the resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/resources", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "application_id": application_id,
                    "application_type": application_type,
                    "credential_provider_id": credential_provider_id,
                    "description": description,
                    "metadata": metadata,
                    "scopes": scopes,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
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
    ) -> Resource:
        """
        Returns details of a specific Resource by ID

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        application_id: Optional[str] | Omit = omit,
        application_type: Literal["native", "web"] | Omit = omit,
        credential_provider_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[MetadataUpdateParam] | Omit = omit,
        name: str | Omit = omit,
        scopes: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resource:
        """
        Updates a Resource's configuration and metadata

        Args:
          application_id: ID of the application that provides this resource (set to null to unset)

          application_type: The expected type of client for this credential. Native clients must use
              localhost URLs for redirect_uris or URIs with custom schemes. Web clients must
              use https URLs and must not use localhost as the hostname.

          credential_provider_id: ID of the credential provider to associate with the resource (set to null to
              unset)

          description: Human-readable description. Must not contain HTML tags (e.g. `<script>`,
              `<div>`) or control characters.

          identifier: User specified identifier, unique within the zone. Must not contain HTML tags
              (e.g. `<script>`, `<div>`) or control characters.

          metadata: Entity metadata (set to null or {} to remove metadata)

          name: Human-readable name. Must not contain HTML tags (e.g. `<script>`, `<div>`) or
              control characters.

          scopes: Scopes supported by the resource (set to null to unset)

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            body=await async_maybe_transform(
                {
                    "application_id": application_id,
                    "application_type": application_type,
                    "credential_provider_id": credential_provider_id,
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "scopes": scopes,
                },
                resource_update_params.ResourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resource,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        credential_provider_id: str | Omit = omit,
        expand: Union[Literal["total_count"], List[Literal["total_count"]]] | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceListResponse:
        """
        Returns a list of resources in the specified zone

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          credential_provider_id: Filter resources by credential provider ID

          identifier: Filter resources by identifier

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/resources", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "credential_provider_id": credential_provider_id,
                        "expand": expand,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            cast_to=ResourceListResponse,
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
        Permanently deletes a Resource

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
            path_template("/zones/{zone_id}/resources/{id}", zone_id=zone_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_raw_response_wrapper(
            resources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            resources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            resources.update,
        )
        self.list = to_raw_response_wrapper(
            resources.list,
        )
        self.delete = to_raw_response_wrapper(
            resources.delete,
        )


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_raw_response_wrapper(
            resources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            resources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            resources.update,
        )
        self.list = async_to_raw_response_wrapper(
            resources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resources.delete,
        )


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_streamed_response_wrapper(
            resources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            resources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            resources.update,
        )
        self.list = to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = to_streamed_response_wrapper(
            resources.delete,
        )


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_streamed_response_wrapper(
            resources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            resources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            resources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resources.delete,
        )
