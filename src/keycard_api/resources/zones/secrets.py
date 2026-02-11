# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import secret_list_params, secret_create_params, secret_update_params
from ..._base_client import make_request_options
from ...types.zones.secret import Secret
from ...types.zones.secret_list_response import SecretListResponse
from ...types.zones.secret_retrieve_response import SecretRetrieveResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        path_zone_id: str,
        *,
        data: secret_create_params.Data,
        entity_id: str,
        name: str,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        body_zone_id: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Args:
          path_zone_id: A globally unique opaque identifier

          entity_id: A globally unique opaque identifier

          name: A name for the entity to be displayed in UI

          description: A description of the entity

          metadata: A JSON object containing arbitrary metadata. Metadata will not be encrypted.

          body_zone_id: Optional zone ID. This field is provided for API compatibility but is ignored
              during processing. The zone ID is derived from the path parameter
              (/zones/{zone_id}/secrets) and takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_zone_id:
            raise ValueError(f"Expected a non-empty value for `path_zone_id` but received {path_zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return self._post(
            f"/zones/{path_zone_id}/secrets",
            body=maybe_transform(
                {
                    "data": data,
                    "entity_id": entity_id,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "body_zone_id": body_zone_id,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveResponse:
        """
        Args:
          zone_id: A globally unique opaque identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        zone_id: str,
        data: secret_update_params.Data | Omit = omit,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Args:
          zone_id: A globally unique opaque identifier

          description: A description of the entity

          metadata: A JSON object containing arbitrary metadata. Metadata will not be encrypted.

          name: A name for the entity to be displayed in UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return self._patch(
            f"/zones/{zone_id}/secrets/{id}",
            body=maybe_transform(
                {
                    "data": data,
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    def list(
        self,
        zone_id: str,
        *,
        entity_id: str | Omit = omit,
        type: Literal["token", "password"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """
        Args:
          zone_id: A globally unique opaque identifier

          entity_id: The entity to list all secrets for

          type: The type of secrets to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "type": type,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          zone_id: A globally unique opaque identifier

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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers.update({**self._client._vault_api_bearer_auth})
        return self._delete(
            f"/zones/{zone_id}/secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keycard-api-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        path_zone_id: str,
        *,
        data: secret_create_params.Data,
        entity_id: str,
        name: str,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        body_zone_id: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Args:
          path_zone_id: A globally unique opaque identifier

          entity_id: A globally unique opaque identifier

          name: A name for the entity to be displayed in UI

          description: A description of the entity

          metadata: A JSON object containing arbitrary metadata. Metadata will not be encrypted.

          body_zone_id: Optional zone ID. This field is provided for API compatibility but is ignored
              during processing. The zone ID is derived from the path parameter
              (/zones/{zone_id}/secrets) and takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_zone_id:
            raise ValueError(f"Expected a non-empty value for `path_zone_id` but received {path_zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return await self._post(
            f"/zones/{path_zone_id}/secrets",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "entity_id": entity_id,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "body_zone_id": body_zone_id,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    async def retrieve(
        self,
        id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveResponse:
        """
        Args:
          zone_id: A globally unique opaque identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        zone_id: str,
        data: secret_update_params.Data | Omit = omit,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Secret:
        """
        Args:
          zone_id: A globally unique opaque identifier

          description: A description of the entity

          metadata: A JSON object containing arbitrary metadata. Metadata will not be encrypted.

          name: A name for the entity to be displayed in UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return await self._patch(
            f"/zones/{zone_id}/secrets/{id}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    async def list(
        self,
        zone_id: str,
        *,
        entity_id: str | Omit = omit,
        type: Literal["token", "password"] | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """
        Args:
          zone_id: A globally unique opaque identifier

          entity_id: The entity to list all secrets for

          type: The type of secrets to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers = {**self._client._vault_api_bearer_auth, **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_id": entity_id,
                        "type": type,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        zone_id: str,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          zone_id: A globally unique opaque identifier

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
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        extra_headers.update({**self._client._vault_api_bearer_auth})
        return await self._delete(
            f"/zones/{zone_id}/secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            secrets.update,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
