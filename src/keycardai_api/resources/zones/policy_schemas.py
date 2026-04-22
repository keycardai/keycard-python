# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...types.zones import policy_schema_list_params, policy_schema_retrieve_params, policy_schema_set_default_params
from ..._base_client import make_request_options
from ...types.zones.policy_schema_list_response import PolicySchemaListResponse
from ...types.zones.schema_version_with_zone_info import SchemaVersionWithZoneInfo

__all__ = ["PolicySchemasResource", "AsyncPolicySchemasResource"]


class PolicySchemasResource(SyncAPIResource):
    """Zone-scoped Cedar schema management.

    The Cedar schema defines the entity model used for authorization decisions.
    Key entity types and their attributes:

    - **Keycard::User** — `email` (String), `groups` (Set of String)
    - **Keycard::Application** — `registration_method` (RegistrationMethod entity), `credential_type` (CredentialType entity)
    - **Keycard::RegistrationMethod** — enum entity: `"managed"`, `"dcr"`
    - **Keycard::CredentialType** — enum entity: `"token"`, `"password"`, `"public-key"`, `"url"`, `"public"`
    - **Keycard::Resource** — `id` (String), `name` (String), `scopes` (Set of String)
    - **Keycard::Claims** — `email` (String), `groups` (Set of String), plus arbitrary additional fields

    Enum-like attributes use Cedar enum entity types (schema version `2026-03-16`+).
    In policies, reference values as `RegistrationMethod::"managed"` or `CredentialType::"token"`.
    See the Credentials API spec for the full entity model reference.
    """

    @cached_property
    def with_raw_response(self) -> PolicySchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicySchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicySchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicySchemasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        version: str,
        *,
        zone_id: str,
        format: Literal["cedar", "json"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaVersionWithZoneInfo:
        """Get a policy schema by version

        Args:
          format: Schema representation format.

        `cedar` returns human-readable Cedar syntax in
              `cedar_schema`, `json` returns Cedar JSON schema object in `cedar_schema_json`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
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
            path_template("/zones/{zone_id}/policy-schemas/{version}", zone_id=zone_id, version=version),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, policy_schema_retrieve_params.PolicySchemaRetrieveParams),
            ),
            cast_to=SchemaVersionWithZoneInfo,
        )

    def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_default: bool | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        is_default: bool | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySchemaListResponse:
        """List policy schemas

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

          filter_default: Filter schemas by default status. When `true`, returns only the zone's default
              schema. When `false`, returns only non-default schemas. Omit to return all
              schemas.

          format: Schema representation format. `cedar` returns human-readable Cedar syntax in
              `cedar_schema`, `json` returns Cedar JSON schema object in `cedar_schema_json`.

          is_default: **Deprecated.** Use `filter[default]` instead.

              Filter schemas by default status. When `true`, returns only the zone's default
              schema. When `false`, returns only non-default schemas. Omit to return all
              schemas.

              Still honored for backward compatibility. Supplying both `is_default` and
              `filter[default]` with conflicting values returns `400 Bad Request`.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

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
            path_template("/zones/{zone_id}/policy-schemas", zone_id=zone_id),
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
                        "filter_default": filter_default,
                        "format": format,
                        "is_default": is_default,
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    policy_schema_list_params.PolicySchemaListParams,
                ),
            ),
            cast_to=PolicySchemaListResponse,
        )

    def set_default(
        self,
        version: str,
        *,
        zone_id: str,
        body: object | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaVersionWithZoneInfo:
        """
        Set the default policy schema for a zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/zones/{zone_id}/policy-schemas/{version}", zone_id=zone_id, version=version),
            body=maybe_transform(body, policy_schema_set_default_params.PolicySchemaSetDefaultParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaVersionWithZoneInfo,
        )


class AsyncPolicySchemasResource(AsyncAPIResource):
    """Zone-scoped Cedar schema management.

    The Cedar schema defines the entity model used for authorization decisions.
    Key entity types and their attributes:

    - **Keycard::User** — `email` (String), `groups` (Set of String)
    - **Keycard::Application** — `registration_method` (RegistrationMethod entity), `credential_type` (CredentialType entity)
    - **Keycard::RegistrationMethod** — enum entity: `"managed"`, `"dcr"`
    - **Keycard::CredentialType** — enum entity: `"token"`, `"password"`, `"public-key"`, `"url"`, `"public"`
    - **Keycard::Resource** — `id` (String), `name` (String), `scopes` (Set of String)
    - **Keycard::Claims** — `email` (String), `groups` (Set of String), plus arbitrary additional fields

    Enum-like attributes use Cedar enum entity types (schema version `2026-03-16`+).
    In policies, reference values as `RegistrationMethod::"managed"` or `CredentialType::"token"`.
    See the Credentials API spec for the full entity model reference.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPolicySchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicySchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicySchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicySchemasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        version: str,
        *,
        zone_id: str,
        format: Literal["cedar", "json"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaVersionWithZoneInfo:
        """Get a policy schema by version

        Args:
          format: Schema representation format.

        `cedar` returns human-readable Cedar syntax in
              `cedar_schema`, `json` returns Cedar JSON schema object in `cedar_schema_json`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
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
            path_template("/zones/{zone_id}/policy-schemas/{version}", zone_id=zone_id, version=version),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, policy_schema_retrieve_params.PolicySchemaRetrieveParams
                ),
            ),
            cast_to=SchemaVersionWithZoneInfo,
        )

    async def list(
        self,
        zone_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        filter_default: bool | Omit = omit,
        format: Literal["cedar", "json"] | Omit = omit,
        is_default: bool | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["created_at"] | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySchemaListResponse:
        """List policy schemas

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

          filter_default: Filter schemas by default status. When `true`, returns only the zone's default
              schema. When `false`, returns only non-default schemas. Omit to return all
              schemas.

          format: Schema representation format. `cedar` returns human-readable Cedar syntax in
              `cedar_schema`, `json` returns Cedar JSON schema object in `cedar_schema_json`.

          is_default: **Deprecated.** Use `filter[default]` instead.

              Filter schemas by default status. When `true`, returns only the zone's default
              schema. When `false`, returns only non-default schemas. Omit to return all
              schemas.

              Still honored for backward compatibility. Supplying both `is_default` and
              `filter[default]` with conflicting values returns `400 Bad Request`.

          limit: Maximum number of items to return per page.

          order: Sort direction. Default is desc (newest first).

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
            path_template("/zones/{zone_id}/policy-schemas", zone_id=zone_id),
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
                        "filter_default": filter_default,
                        "format": format,
                        "is_default": is_default,
                        "limit": limit,
                        "order": order,
                        "sort": sort,
                    },
                    policy_schema_list_params.PolicySchemaListParams,
                ),
            ),
            cast_to=PolicySchemaListResponse,
        )

    async def set_default(
        self,
        version: str,
        *,
        zone_id: str,
        body: object | Omit = omit,
        x_api_version: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaVersionWithZoneInfo:
        """
        Set the default policy schema for a zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": x_api_version,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/zones/{zone_id}/policy-schemas/{version}", zone_id=zone_id, version=version),
            body=await async_maybe_transform(body, policy_schema_set_default_params.PolicySchemaSetDefaultParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaVersionWithZoneInfo,
        )


class PolicySchemasResourceWithRawResponse:
    def __init__(self, policy_schemas: PolicySchemasResource) -> None:
        self._policy_schemas = policy_schemas

        self.retrieve = to_raw_response_wrapper(
            policy_schemas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            policy_schemas.list,
        )
        self.set_default = to_raw_response_wrapper(
            policy_schemas.set_default,
        )


class AsyncPolicySchemasResourceWithRawResponse:
    def __init__(self, policy_schemas: AsyncPolicySchemasResource) -> None:
        self._policy_schemas = policy_schemas

        self.retrieve = async_to_raw_response_wrapper(
            policy_schemas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            policy_schemas.list,
        )
        self.set_default = async_to_raw_response_wrapper(
            policy_schemas.set_default,
        )


class PolicySchemasResourceWithStreamingResponse:
    def __init__(self, policy_schemas: PolicySchemasResource) -> None:
        self._policy_schemas = policy_schemas

        self.retrieve = to_streamed_response_wrapper(
            policy_schemas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            policy_schemas.list,
        )
        self.set_default = to_streamed_response_wrapper(
            policy_schemas.set_default,
        )


class AsyncPolicySchemasResourceWithStreamingResponse:
    def __init__(self, policy_schemas: AsyncPolicySchemasResource) -> None:
        self._policy_schemas = policy_schemas

        self.retrieve = async_to_streamed_response_wrapper(
            policy_schemas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_schemas.list,
        )
        self.set_default = async_to_streamed_response_wrapper(
            policy_schemas.set_default,
        )
