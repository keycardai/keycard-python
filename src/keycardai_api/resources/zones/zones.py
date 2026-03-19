# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import (
    zone_list_params,
    zone_create_params,
    zone_update_params,
    zone_retrieve_params,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .providers import (
    ProvidersResource,
    AsyncProvidersResource,
    ProvidersResourceWithRawResponse,
    AsyncProvidersResourceWithRawResponse,
    ProvidersResourceWithStreamingResponse,
    AsyncProvidersResourceWithStreamingResponse,
)
from .resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .user_agents import (
    UserAgentsResource,
    AsyncUserAgentsResource,
    UserAgentsResourceWithRawResponse,
    AsyncUserAgentsResourceWithRawResponse,
    UserAgentsResourceWithStreamingResponse,
    AsyncUserAgentsResourceWithStreamingResponse,
)
from ...types.zone import Zone
from ..._base_client import make_request_options
from .policy_schemas import (
    PolicySchemasResource,
    AsyncPolicySchemasResource,
    PolicySchemasResourceWithRawResponse,
    AsyncPolicySchemasResourceWithRawResponse,
    PolicySchemasResourceWithStreamingResponse,
    AsyncPolicySchemasResourceWithStreamingResponse,
)
from .delegated_grants import (
    DelegatedGrantsResource,
    AsyncDelegatedGrantsResource,
    DelegatedGrantsResourceWithRawResponse,
    AsyncDelegatedGrantsResourceWithRawResponse,
    DelegatedGrantsResourceWithStreamingResponse,
    AsyncDelegatedGrantsResourceWithStreamingResponse,
)
from .policies.policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from .application_credentials import (
    ApplicationCredentialsResource,
    AsyncApplicationCredentialsResource,
    ApplicationCredentialsResourceWithRawResponse,
    AsyncApplicationCredentialsResourceWithRawResponse,
    ApplicationCredentialsResourceWithStreamingResponse,
    AsyncApplicationCredentialsResourceWithStreamingResponse,
)
from .policy_sets.policy_sets import (
    PolicySetsResource,
    AsyncPolicySetsResource,
    PolicySetsResourceWithRawResponse,
    AsyncPolicySetsResourceWithRawResponse,
    PolicySetsResourceWithStreamingResponse,
    AsyncPolicySetsResourceWithStreamingResponse,
)
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)
from ...types.zone_list_response import ZoneListResponse
from ...types.encryption_key_aws_kms_config_param import EncryptionKeyAwsKmsConfigParam

__all__ = ["ZonesResource", "AsyncZonesResource"]


class ZonesResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def application_credentials(self) -> ApplicationCredentialsResource:
        return ApplicationCredentialsResource(self._client)

    @cached_property
    def delegated_grants(self) -> DelegatedGrantsResource:
        return DelegatedGrantsResource(self._client)

    @cached_property
    def providers(self) -> ProvidersResource:
        return ProvidersResource(self._client)

    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def user_agents(self) -> UserAgentsResource:
        return UserAgentsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def policy_schemas(self) -> PolicySchemasResource:
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
        return PolicySchemasResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        """Policy CRUD operations"""
        return PoliciesResource(self._client)

    @cached_property
    def policy_sets(self) -> PolicySetsResource:
        """Policy set CRUD and binding management"""
        return PolicySetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return ZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return ZonesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        default_mcp_gateway_application: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        encryption_key: EncryptionKeyAwsKmsConfigParam | Omit = omit,
        login_flow: Literal["default", "identifier_first"] | Omit = omit,
        protocols: zone_create_params.Protocols | Omit = omit,
        requires_invitation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """Creates a new zone for the authenticated organization.

        A zone is an isolated
        environment for IAM resources.

        Args:
          name: Human-readable name

          default_mcp_gateway_application: Assign a default MCP Gateway application to the zone

          description: Human-readable description

          encryption_key: AWS KMS configuration for zone encryption. When not specified, the default
              Keycard Cloud encryption key will be used.

          login_flow: Login flow style for the zone. 'default' uses standard authentication,
              'identifier_first' uses identifier-based provider routing.

          protocols: Protocol configuration for zone creation

          requires_invitation: Whether the zone requires an invitation for email/password registration, only
              applies when user_identity_provider_id is not set. Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/zones",
            body=maybe_transform(
                {
                    "name": name,
                    "default_mcp_gateway_application": default_mcp_gateway_application,
                    "description": description,
                    "encryption_key": encryption_key,
                    "login_flow": login_flow,
                    "protocols": protocols,
                    "requires_invitation": requires_invitation,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Zone,
        )

    def retrieve(
        self,
        zone_id: str,
        *,
        expand: Union[Literal["permissions"], List[Literal["permissions"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """
        Returns details of a specific zone by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, zone_retrieve_params.ZoneRetrieveParams),
            ),
            cast_to=Zone,
        )

    def update(
        self,
        zone_id: str,
        *,
        default_mcp_gateway_application_id: Optional[str] | Omit = omit,
        default_resource_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        encryption_key: Optional[zone_update_params.EncryptionKey] | Omit = omit,
        login_flow: Optional[Literal["default", "identifier_first"]] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[zone_update_params.Protocols] | Omit = omit,
        requires_invitation: bool | Omit = omit,
        user_identity_provider_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """
        Updates a zone's configuration (partial update)

        Args:
          default_mcp_gateway_application_id: Application ID configured as the default MCP Gateway for the zone (set to null
              to unset)

          default_resource_id: Resource ID to configure as the default resource for the zone (set to null to
              unset)

          description: Human-readable description

          encryption_key: AWS KMS configuration for zone encryption update (set to null to remove
              customer-managed key and revert to default)

          login_flow: Login flow style for the zone. 'default' uses standard authentication,
              'identifier_first' uses identifier-based provider routing. Set to null to reset
              to 'default'.

          name: Human-readable name

          protocols: Protocol configuration update for a zone (partial update)

          requires_invitation: Whether the zone requires an invitation for email/password registration, only
              applies when user_identity_provider_id is not set

          user_identity_provider_id: Provider ID to configure for user login (set to null to unset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            body=maybe_transform(
                {
                    "default_mcp_gateway_application_id": default_mcp_gateway_application_id,
                    "default_resource_id": default_resource_id,
                    "description": description,
                    "encryption_key": encryption_key,
                    "login_flow": login_flow,
                    "name": name,
                    "protocols": protocols,
                    "requires_invitation": requires_invitation,
                    "user_identity_provider_id": user_identity_provider_id,
                },
                zone_update_params.ZoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Zone,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        cursor: str | Omit = omit,
        expand: Union[Literal["total_count", "permissions"], List[Literal["total_count", "permissions"]]] | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneListResponse:
        """
        Returns a list of zones for the authenticated organization

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/zones",
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
                        "limit": limit,
                        "slug": slug,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            cast_to=ZoneListResponse,
        )

    def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a zone and all its associated resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncZonesResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def application_credentials(self) -> AsyncApplicationCredentialsResource:
        return AsyncApplicationCredentialsResource(self._client)

    @cached_property
    def delegated_grants(self) -> AsyncDelegatedGrantsResource:
        return AsyncDelegatedGrantsResource(self._client)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        return AsyncProvidersResource(self._client)

    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def user_agents(self) -> AsyncUserAgentsResource:
        return AsyncUserAgentsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def policy_schemas(self) -> AsyncPolicySchemasResource:
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
        return AsyncPolicySchemasResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        """Policy CRUD operations"""
        return AsyncPoliciesResource(self._client)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResource:
        """Policy set CRUD and binding management"""
        return AsyncPolicySetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncZonesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        default_mcp_gateway_application: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        encryption_key: EncryptionKeyAwsKmsConfigParam | Omit = omit,
        login_flow: Literal["default", "identifier_first"] | Omit = omit,
        protocols: zone_create_params.Protocols | Omit = omit,
        requires_invitation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """Creates a new zone for the authenticated organization.

        A zone is an isolated
        environment for IAM resources.

        Args:
          name: Human-readable name

          default_mcp_gateway_application: Assign a default MCP Gateway application to the zone

          description: Human-readable description

          encryption_key: AWS KMS configuration for zone encryption. When not specified, the default
              Keycard Cloud encryption key will be used.

          login_flow: Login flow style for the zone. 'default' uses standard authentication,
              'identifier_first' uses identifier-based provider routing.

          protocols: Protocol configuration for zone creation

          requires_invitation: Whether the zone requires an invitation for email/password registration, only
              applies when user_identity_provider_id is not set. Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/zones",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "default_mcp_gateway_application": default_mcp_gateway_application,
                    "description": description,
                    "encryption_key": encryption_key,
                    "login_flow": login_flow,
                    "protocols": protocols,
                    "requires_invitation": requires_invitation,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Zone,
        )

    async def retrieve(
        self,
        zone_id: str,
        *,
        expand: Union[Literal["permissions"], List[Literal["permissions"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """
        Returns details of a specific zone by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, zone_retrieve_params.ZoneRetrieveParams),
            ),
            cast_to=Zone,
        )

    async def update(
        self,
        zone_id: str,
        *,
        default_mcp_gateway_application_id: Optional[str] | Omit = omit,
        default_resource_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        encryption_key: Optional[zone_update_params.EncryptionKey] | Omit = omit,
        login_flow: Optional[Literal["default", "identifier_first"]] | Omit = omit,
        name: str | Omit = omit,
        protocols: Optional[zone_update_params.Protocols] | Omit = omit,
        requires_invitation: bool | Omit = omit,
        user_identity_provider_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Zone:
        """
        Updates a zone's configuration (partial update)

        Args:
          default_mcp_gateway_application_id: Application ID configured as the default MCP Gateway for the zone (set to null
              to unset)

          default_resource_id: Resource ID to configure as the default resource for the zone (set to null to
              unset)

          description: Human-readable description

          encryption_key: AWS KMS configuration for zone encryption update (set to null to remove
              customer-managed key and revert to default)

          login_flow: Login flow style for the zone. 'default' uses standard authentication,
              'identifier_first' uses identifier-based provider routing. Set to null to reset
              to 'default'.

          name: Human-readable name

          protocols: Protocol configuration update for a zone (partial update)

          requires_invitation: Whether the zone requires an invitation for email/password registration, only
              applies when user_identity_provider_id is not set

          user_identity_provider_id: Provider ID to configure for user login (set to null to unset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "default_mcp_gateway_application_id": default_mcp_gateway_application_id,
                    "default_resource_id": default_resource_id,
                    "description": description,
                    "encryption_key": encryption_key,
                    "login_flow": login_flow,
                    "name": name,
                    "protocols": protocols,
                    "requires_invitation": requires_invitation,
                    "user_identity_provider_id": user_identity_provider_id,
                },
                zone_update_params.ZoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Zone,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        cursor: str | Omit = omit,
        expand: Union[Literal["total_count", "permissions"], List[Literal["total_count", "permissions"]]] | Omit = omit,
        limit: int | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZoneListResponse:
        """
        Returns a list of zones for the authenticated organization

        Args:
          after: Cursor for forward pagination

          before: Cursor for backward pagination

          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/zones",
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
                        "limit": limit,
                        "slug": slug,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            cast_to=ZoneListResponse,
        )

    async def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a zone and all its associated resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/zones/{zone_id}", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ZonesResourceWithRawResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.create = to_raw_response_wrapper(
            zones.create,
        )
        self.retrieve = to_raw_response_wrapper(
            zones.retrieve,
        )
        self.update = to_raw_response_wrapper(
            zones.update,
        )
        self.list = to_raw_response_wrapper(
            zones.list,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._zones.applications)

    @cached_property
    def application_credentials(self) -> ApplicationCredentialsResourceWithRawResponse:
        return ApplicationCredentialsResourceWithRawResponse(self._zones.application_credentials)

    @cached_property
    def delegated_grants(self) -> DelegatedGrantsResourceWithRawResponse:
        return DelegatedGrantsResourceWithRawResponse(self._zones.delegated_grants)

    @cached_property
    def providers(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self._zones.providers)

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._zones.resources)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._zones.sessions)

    @cached_property
    def user_agents(self) -> UserAgentsResourceWithRawResponse:
        return UserAgentsResourceWithRawResponse(self._zones.user_agents)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._zones.users)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._zones.members)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._zones.secrets)

    @cached_property
    def policy_schemas(self) -> PolicySchemasResourceWithRawResponse:
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
        return PolicySchemasResourceWithRawResponse(self._zones.policy_schemas)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        """Policy CRUD operations"""
        return PoliciesResourceWithRawResponse(self._zones.policies)

    @cached_property
    def policy_sets(self) -> PolicySetsResourceWithRawResponse:
        """Policy set CRUD and binding management"""
        return PolicySetsResourceWithRawResponse(self._zones.policy_sets)


class AsyncZonesResourceWithRawResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.create = async_to_raw_response_wrapper(
            zones.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            zones.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            zones.update,
        )
        self.list = async_to_raw_response_wrapper(
            zones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._zones.applications)

    @cached_property
    def application_credentials(self) -> AsyncApplicationCredentialsResourceWithRawResponse:
        return AsyncApplicationCredentialsResourceWithRawResponse(self._zones.application_credentials)

    @cached_property
    def delegated_grants(self) -> AsyncDelegatedGrantsResourceWithRawResponse:
        return AsyncDelegatedGrantsResourceWithRawResponse(self._zones.delegated_grants)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self._zones.providers)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._zones.resources)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._zones.sessions)

    @cached_property
    def user_agents(self) -> AsyncUserAgentsResourceWithRawResponse:
        return AsyncUserAgentsResourceWithRawResponse(self._zones.user_agents)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._zones.users)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._zones.members)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._zones.secrets)

    @cached_property
    def policy_schemas(self) -> AsyncPolicySchemasResourceWithRawResponse:
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
        return AsyncPolicySchemasResourceWithRawResponse(self._zones.policy_schemas)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        """Policy CRUD operations"""
        return AsyncPoliciesResourceWithRawResponse(self._zones.policies)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResourceWithRawResponse:
        """Policy set CRUD and binding management"""
        return AsyncPolicySetsResourceWithRawResponse(self._zones.policy_sets)


class ZonesResourceWithStreamingResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.create = to_streamed_response_wrapper(
            zones.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            zones.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            zones.update,
        )
        self.list = to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._zones.applications)

    @cached_property
    def application_credentials(self) -> ApplicationCredentialsResourceWithStreamingResponse:
        return ApplicationCredentialsResourceWithStreamingResponse(self._zones.application_credentials)

    @cached_property
    def delegated_grants(self) -> DelegatedGrantsResourceWithStreamingResponse:
        return DelegatedGrantsResourceWithStreamingResponse(self._zones.delegated_grants)

    @cached_property
    def providers(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self._zones.providers)

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._zones.resources)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._zones.sessions)

    @cached_property
    def user_agents(self) -> UserAgentsResourceWithStreamingResponse:
        return UserAgentsResourceWithStreamingResponse(self._zones.user_agents)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._zones.users)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._zones.members)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._zones.secrets)

    @cached_property
    def policy_schemas(self) -> PolicySchemasResourceWithStreamingResponse:
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
        return PolicySchemasResourceWithStreamingResponse(self._zones.policy_schemas)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        """Policy CRUD operations"""
        return PoliciesResourceWithStreamingResponse(self._zones.policies)

    @cached_property
    def policy_sets(self) -> PolicySetsResourceWithStreamingResponse:
        """Policy set CRUD and binding management"""
        return PolicySetsResourceWithStreamingResponse(self._zones.policy_sets)


class AsyncZonesResourceWithStreamingResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.create = async_to_streamed_response_wrapper(
            zones.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            zones.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            zones.update,
        )
        self.list = async_to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._zones.applications)

    @cached_property
    def application_credentials(self) -> AsyncApplicationCredentialsResourceWithStreamingResponse:
        return AsyncApplicationCredentialsResourceWithStreamingResponse(self._zones.application_credentials)

    @cached_property
    def delegated_grants(self) -> AsyncDelegatedGrantsResourceWithStreamingResponse:
        return AsyncDelegatedGrantsResourceWithStreamingResponse(self._zones.delegated_grants)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self._zones.providers)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._zones.resources)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._zones.sessions)

    @cached_property
    def user_agents(self) -> AsyncUserAgentsResourceWithStreamingResponse:
        return AsyncUserAgentsResourceWithStreamingResponse(self._zones.user_agents)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._zones.users)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._zones.members)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._zones.secrets)

    @cached_property
    def policy_schemas(self) -> AsyncPolicySchemasResourceWithStreamingResponse:
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
        return AsyncPolicySchemasResourceWithStreamingResponse(self._zones.policy_schemas)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """Policy CRUD operations"""
        return AsyncPoliciesResourceWithStreamingResponse(self._zones.policies)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResourceWithStreamingResponse:
        """Policy set CRUD and binding management"""
        return AsyncPolicySetsResourceWithStreamingResponse(self._zones.policy_sets)
