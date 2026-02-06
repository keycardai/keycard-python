# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .dependencies import (
    DependenciesResource,
    AsyncDependenciesResource,
    DependenciesResourceWithRawResponse,
    AsyncDependenciesResourceWithRawResponse,
    DependenciesResourceWithStreamingResponse,
    AsyncDependenciesResourceWithStreamingResponse,
)
from ....types.zones import (
    application_list_params,
    application_create_params,
    application_update_params,
    application_list_resources_params,
    application_list_credentials_params,
)
from ...._base_client import make_request_options
from ....types.zones.application import Application
from ....types.zones.metadata_param import MetadataParam
from ....types.zones.application_trait import ApplicationTrait
from ....types.zones.metadata_update_param import MetadataUpdateParam
from ....types.zones.application_list_response import ApplicationListResponse
from ....types.zones.application_list_resources_response import ApplicationListResourcesResponse
from ....types.zones.application_list_credentials_response import ApplicationListCredentialsResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def dependencies(self) -> DependenciesResource:
        return DependenciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        dependencies: Iterable[application_create_params.Dependency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        protocols: application_create_params.Protocols | Omit = omit,
        traits: List[ApplicationTrait] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Application:
        """
        Creates a new Application - a software system with an identity that can access
        Resources

        Args:
          identifier: User specified identifier, unique within the zone

          name: Human-readable name

          dependencies: Dependencies of the application

          description: Human-readable description

          metadata: Entity metadata

          protocols: Protocol-specific configuration for application creation

          traits: Traits of the application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/applications",
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "dependencies": dependencies,
                    "description": description,
                    "metadata": metadata,
                    "protocols": protocols,
                    "traits": traits,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
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
    ) -> Application:
        """
        Returns details of a specific Application by ID

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
            f"/zones/{zone_id}/applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
        )

    def update(
        self,
        id: str,
        *,
        zone_id: str,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[MetadataUpdateParam] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[application_update_params.Protocols] | Omit = omit,
        traits: Optional[List[ApplicationTrait]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Application:
        """
        Updates an Application's configuration and metadata

        Args:
          description: Human-readable description

          identifier: User specified identifier, unique within the zone

          metadata: Entity metadata (set to null or {} to remove metadata)

          name: Human-readable name

          protocols: Protocol-specific configuration for application update

          traits: Traits of the application

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
            f"/zones/{zone_id}/applications/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "protocols": protocols,
                    "traits": traits,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
        )

    def list(
        self,
        zone_id: str,
        *,
        cursor: str | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        traits: List[ApplicationTrait] | Omit = omit,
        traits_all: List[ApplicationTrait] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResponse:
        """
        Returns a list of applications in the specified zone

        Args:
          traits: Filter by traits (OR matching - returns applications with any of the specified
              traits)

          traits_all: Filter by traits (AND matching - returns applications with all of the specified
              traits)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/applications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                        "traits": traits,
                        "traits_all": traits_all,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            cast_to=ApplicationListResponse,
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
        Permanently deletes an application

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
            f"/zones/{zone_id}/applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_credentials(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListCredentialsResponse:
        """
        Returns a list of application credentials for a specific application

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
            f"/zones/{zone_id}/applications/{id}/application-credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    application_list_credentials_params.ApplicationListCredentialsParams,
                ),
            ),
            cast_to=ApplicationListCredentialsResponse,
        )

    def list_resources(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResourcesResponse:
        """
        Returns a list of resources provided by an application

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
            f"/zones/{zone_id}/applications/{id}/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    application_list_resources_params.ApplicationListResourcesParams,
                ),
            ),
            cast_to=ApplicationListResourcesResponse,
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def dependencies(self) -> AsyncDependenciesResource:
        return AsyncDependenciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        identifier: str,
        name: str,
        dependencies: Iterable[application_create_params.Dependency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        protocols: application_create_params.Protocols | Omit = omit,
        traits: List[ApplicationTrait] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Application:
        """
        Creates a new Application - a software system with an identity that can access
        Resources

        Args:
          identifier: User specified identifier, unique within the zone

          name: Human-readable name

          dependencies: Dependencies of the application

          description: Human-readable description

          metadata: Entity metadata

          protocols: Protocol-specific configuration for application creation

          traits: Traits of the application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/applications",
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "name": name,
                    "dependencies": dependencies,
                    "description": description,
                    "metadata": metadata,
                    "protocols": protocols,
                    "traits": traits,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
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
    ) -> Application:
        """
        Returns details of a specific Application by ID

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
            f"/zones/{zone_id}/applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
        )

    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        description: Optional[str] | Omit = omit,
        identifier: str | Omit = omit,
        metadata: Optional[MetadataUpdateParam] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[application_update_params.Protocols] | Omit = omit,
        traits: Optional[List[ApplicationTrait]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Application:
        """
        Updates an Application's configuration and metadata

        Args:
          description: Human-readable description

          identifier: User specified identifier, unique within the zone

          metadata: Entity metadata (set to null or {} to remove metadata)

          name: Human-readable name

          protocols: Protocol-specific configuration for application update

          traits: Traits of the application

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
            f"/zones/{zone_id}/applications/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "identifier": identifier,
                    "metadata": metadata,
                    "name": name,
                    "protocols": protocols,
                    "traits": traits,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Application,
        )

    async def list(
        self,
        zone_id: str,
        *,
        cursor: str | Omit = omit,
        identifier: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        traits: List[ApplicationTrait] | Omit = omit,
        traits_all: List[ApplicationTrait] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResponse:
        """
        Returns a list of applications in the specified zone

        Args:
          traits: Filter by traits (OR matching - returns applications with any of the specified
              traits)

          traits_all: Filter by traits (AND matching - returns applications with all of the specified
              traits)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/applications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "identifier": identifier,
                        "limit": limit,
                        "slug": slug,
                        "traits": traits,
                        "traits_all": traits_all,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            cast_to=ApplicationListResponse,
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
        Permanently deletes an application

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
            f"/zones/{zone_id}/applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_credentials(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListCredentialsResponse:
        """
        Returns a list of application credentials for a specific application

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
            f"/zones/{zone_id}/applications/{id}/application-credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    application_list_credentials_params.ApplicationListCredentialsParams,
                ),
            ),
            cast_to=ApplicationListCredentialsResponse,
        )

    async def list_resources(
        self,
        id: str,
        *,
        zone_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResourcesResponse:
        """
        Returns a list of resources provided by an application

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
            f"/zones/{zone_id}/applications/{id}/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    application_list_resources_params.ApplicationListResourcesParams,
                ),
            ),
            cast_to=ApplicationListResourcesResponse,
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_raw_response_wrapper(
            applications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            applications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            applications.update,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.delete = to_raw_response_wrapper(
            applications.delete,
        )
        self.list_credentials = to_raw_response_wrapper(
            applications.list_credentials,
        )
        self.list_resources = to_raw_response_wrapper(
            applications.list_resources,
        )

    @cached_property
    def dependencies(self) -> DependenciesResourceWithRawResponse:
        return DependenciesResourceWithRawResponse(self._applications.dependencies)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_raw_response_wrapper(
            applications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            applications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            applications.delete,
        )
        self.list_credentials = async_to_raw_response_wrapper(
            applications.list_credentials,
        )
        self.list_resources = async_to_raw_response_wrapper(
            applications.list_resources,
        )

    @cached_property
    def dependencies(self) -> AsyncDependenciesResourceWithRawResponse:
        return AsyncDependenciesResourceWithRawResponse(self._applications.dependencies)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_streamed_response_wrapper(
            applications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            applications.update,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            applications.delete,
        )
        self.list_credentials = to_streamed_response_wrapper(
            applications.list_credentials,
        )
        self.list_resources = to_streamed_response_wrapper(
            applications.list_resources,
        )

    @cached_property
    def dependencies(self) -> DependenciesResourceWithStreamingResponse:
        return DependenciesResourceWithStreamingResponse(self._applications.dependencies)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_streamed_response_wrapper(
            applications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            applications.delete,
        )
        self.list_credentials = async_to_streamed_response_wrapper(
            applications.list_credentials,
        )
        self.list_resources = async_to_streamed_response_wrapper(
            applications.list_resources,
        )

    @cached_property
    def dependencies(self) -> AsyncDependenciesResourceWithStreamingResponse:
        return AsyncDependenciesResourceWithStreamingResponse(self._applications.dependencies)
