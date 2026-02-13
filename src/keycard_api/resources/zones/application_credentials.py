# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import (
    application_credential_list_params,
    application_credential_create_params,
    application_credential_update_params,
)
from ..._base_client import make_request_options
from ...types.zones.credential import Credential
from ...types.zones.application_credential_list_response import ApplicationCredentialListResponse
from ...types.zones.application_credential_create_response import ApplicationCredentialCreateResponse

__all__ = ["ApplicationCredentialsResource", "AsyncApplicationCredentialsResource"]


class ApplicationCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplicationCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return ApplicationCredentialsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        provider_id: str,
        type: Literal["token"],
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          provider_id: ID of the provider issuing tokens this credential verifies

          subject: Subject identifier for the token. When omitted, any token from the provider is
              accepted without checking application-specific claims.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        type: Literal["password"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: Username for password credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        jwks_uri: str,
        type: Literal["public-key"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          jwks_uri: JWKS URI to retrieve public keys from

          identifier: Client ID for public key credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        identifier: str,
        type: Literal["url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: URL of the credential (must be a valid URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        type: Literal["public"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: Identifier for public credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["application_id", "provider_id", "type"],
        ["application_id", "type"],
        ["application_id", "jwks_uri", "type"],
        ["application_id", "identifier", "type"],
    )
    def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        provider_id: str | Omit = omit,
        type: Literal["token"] | Literal["password"] | Literal["public-key"] | Literal["url"] | Literal["public"],
        subject: str | Omit = omit,
        identifier: str | Omit = omit,
        jwks_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            ApplicationCredentialCreateResponse,
            self._post(
                f"/zones/{zone_id}/application-credentials",
                body=maybe_transform(
                    {
                        "application_id": application_id,
                        "provider_id": provider_id,
                        "type": type,
                        "subject": subject,
                        "identifier": identifier,
                        "jwks_uri": jwks_uri,
                    },
                    application_credential_create_params.ApplicationCredentialCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ApplicationCredentialCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Credential:
        """
        Returns details of a specific application credential by ID

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
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            Credential,
            self._get(
                f"/zones/{zone_id}/application-credentials/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Credential),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        subject: Optional[str] | Omit = omit,
        type: Literal["token"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          subject: Subject identifier for the token. Set to null to unset, which allows any token
              from the provider to be accepted without checking application-specific claims.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        type: Literal["password"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        type: Literal["public-key"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        type: Literal["url"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          identifier: URL of the credential (must be a valid URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        type: Literal["public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          identifier: Identifier for public credential, also used as OAuth 2.0 client ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def update(
        self,
        id: str,
        *,
        zone_id: str,
        subject: Optional[str] | Omit = omit,
        type: Literal["token"]
        | Literal["password"]
        | Literal["public-key"]
        | Literal["url"]
        | Literal["public"]
        | Omit = omit,
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            Credential,
            self._patch(
                f"/zones/{zone_id}/application-credentials/{id}",
                body=maybe_transform(
                    {
                        "subject": subject,
                        "type": type,
                        "identifier": identifier,
                    },
                    application_credential_update_params.ApplicationCredentialUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Credential),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        zone_id: str,
        *,
        application_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialListResponse:
        """
        Returns a list of application credentials in the specified zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/application-credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application_id": application_id,
                        "cursor": cursor,
                        "limit": limit,
                        "slug": slug,
                    },
                    application_credential_list_params.ApplicationCredentialListParams,
                ),
            ),
            cast_to=ApplicationCredentialListResponse,
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
        Permanently deletes an application credential

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
        extra_headers.update({"Authorization": omit})
        return self._delete(
            f"/zones/{zone_id}/application-credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncApplicationCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplicationCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardlabs/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardlabs/keycard-python#with_streaming_response
        """
        return AsyncApplicationCredentialsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        provider_id: str,
        type: Literal["token"],
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          provider_id: ID of the provider issuing tokens this credential verifies

          subject: Subject identifier for the token. When omitted, any token from the provider is
              accepted without checking application-specific claims.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        type: Literal["password"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: Username for password credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        jwks_uri: str,
        type: Literal["public-key"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          jwks_uri: JWKS URI to retrieve public keys from

          identifier: Client ID for public key credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        identifier: str,
        type: Literal["url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: URL of the credential (must be a valid URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        type: Literal["public"],
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        """
        Creates a new application credential

        Args:
          application_id: ID of the application this credential belongs to

          identifier: Identifier for public credential, also used as OAuth 2.0 client ID
              (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["application_id", "provider_id", "type"],
        ["application_id", "type"],
        ["application_id", "jwks_uri", "type"],
        ["application_id", "identifier", "type"],
    )
    async def create(
        self,
        zone_id: str,
        *,
        application_id: str,
        provider_id: str | Omit = omit,
        type: Literal["token"] | Literal["password"] | Literal["public-key"] | Literal["url"] | Literal["public"],
        subject: str | Omit = omit,
        identifier: str | Omit = omit,
        jwks_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialCreateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            ApplicationCredentialCreateResponse,
            await self._post(
                f"/zones/{zone_id}/application-credentials",
                body=await async_maybe_transform(
                    {
                        "application_id": application_id,
                        "provider_id": provider_id,
                        "type": type,
                        "subject": subject,
                        "identifier": identifier,
                        "jwks_uri": jwks_uri,
                    },
                    application_credential_create_params.ApplicationCredentialCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ApplicationCredentialCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Credential:
        """
        Returns details of a specific application credential by ID

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
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            Credential,
            await self._get(
                f"/zones/{zone_id}/application-credentials/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Credential),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        subject: Optional[str] | Omit = omit,
        type: Literal["token"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          subject: Subject identifier for the token. Set to null to unset, which allows any token
              from the provider to be accepted without checking application-specific claims.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        type: Literal["password"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        type: Literal["public-key"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        type: Literal["url"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          identifier: URL of the credential (must be a valid URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        identifier: str | Omit = omit,
        type: Literal["public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Updates an application credential's configuration

        Args:
          identifier: Identifier for public credential, also used as OAuth 2.0 client ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        subject: Optional[str] | Omit = omit,
        type: Literal["token"]
        | Literal["password"]
        | Literal["public-key"]
        | Literal["url"]
        | Literal["public"]
        | Omit = omit,
        identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return cast(
            Credential,
            await self._patch(
                f"/zones/{zone_id}/application-credentials/{id}",
                body=await async_maybe_transform(
                    {
                        "subject": subject,
                        "type": type,
                        "identifier": identifier,
                    },
                    application_credential_update_params.ApplicationCredentialUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Credential),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        zone_id: str,
        *,
        application_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCredentialListResponse:
        """
        Returns a list of application credentials in the specified zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Authorization": omit, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/application-credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "application_id": application_id,
                        "cursor": cursor,
                        "limit": limit,
                        "slug": slug,
                    },
                    application_credential_list_params.ApplicationCredentialListParams,
                ),
            ),
            cast_to=ApplicationCredentialListResponse,
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
        Permanently deletes an application credential

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
        extra_headers.update({"Authorization": omit})
        return await self._delete(
            f"/zones/{zone_id}/application-credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ApplicationCredentialsResourceWithRawResponse:
    def __init__(self, application_credentials: ApplicationCredentialsResource) -> None:
        self._application_credentials = application_credentials

        self.create = to_raw_response_wrapper(
            application_credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            application_credentials.retrieve,
        )
        self.update = to_raw_response_wrapper(
            application_credentials.update,
        )
        self.list = to_raw_response_wrapper(
            application_credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            application_credentials.delete,
        )


class AsyncApplicationCredentialsResourceWithRawResponse:
    def __init__(self, application_credentials: AsyncApplicationCredentialsResource) -> None:
        self._application_credentials = application_credentials

        self.create = async_to_raw_response_wrapper(
            application_credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            application_credentials.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            application_credentials.update,
        )
        self.list = async_to_raw_response_wrapper(
            application_credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            application_credentials.delete,
        )


class ApplicationCredentialsResourceWithStreamingResponse:
    def __init__(self, application_credentials: ApplicationCredentialsResource) -> None:
        self._application_credentials = application_credentials

        self.create = to_streamed_response_wrapper(
            application_credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            application_credentials.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            application_credentials.update,
        )
        self.list = to_streamed_response_wrapper(
            application_credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            application_credentials.delete,
        )


class AsyncApplicationCredentialsResourceWithStreamingResponse:
    def __init__(self, application_credentials: AsyncApplicationCredentialsResource) -> None:
        self._application_credentials = application_credentials

        self.create = async_to_streamed_response_wrapper(
            application_credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            application_credentials.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            application_credentials.update,
        )
        self.list = async_to_streamed_response_wrapper(
            application_credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            application_credentials.delete,
        )
