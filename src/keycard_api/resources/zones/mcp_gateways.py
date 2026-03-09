# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zones import mcp_gateway_create_mcp_server_params
from ..._base_client import make_request_options
from ...types.zones.mcp_gateway_create_mcp_server_response import McpGatewayCreateMcpServerResponse

__all__ = ["McpGatewaysResource", "AsyncMcpGatewaysResource"]


class McpGatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return McpGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return McpGatewaysResourceWithStreamingResponse(self)

    def create_mcp_server(
        self,
        application_id: str,
        *,
        zone_id: str,
        downstream: mcp_gateway_create_mcp_server_params.Downstream,
        upstream: mcp_gateway_create_mcp_server_params.Upstream,
        upstream_provider: mcp_gateway_create_mcp_server_params.UpstreamProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpGatewayCreateMcpServerResponse:
        """
        Creates all resources required to access an MCP server through an MCP gateway

        Args:
          downstream: Downstream MCP server config

          upstream: Upstream MCP server config

          upstream_provider: Credential provider for the upstream connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/zones/{zone_id}/mcp-gateways/{application_id}/mcp-servers",
            body=maybe_transform(
                {
                    "downstream": downstream,
                    "upstream": upstream,
                    "upstream_provider": upstream_provider,
                },
                mcp_gateway_create_mcp_server_params.McpGatewayCreateMcpServerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=McpGatewayCreateMcpServerResponse,
        )


class AsyncMcpGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncMcpGatewaysResourceWithStreamingResponse(self)

    async def create_mcp_server(
        self,
        application_id: str,
        *,
        zone_id: str,
        downstream: mcp_gateway_create_mcp_server_params.Downstream,
        upstream: mcp_gateway_create_mcp_server_params.Upstream,
        upstream_provider: mcp_gateway_create_mcp_server_params.UpstreamProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpGatewayCreateMcpServerResponse:
        """
        Creates all resources required to access an MCP server through an MCP gateway

        Args:
          downstream: Downstream MCP server config

          upstream: Upstream MCP server config

          upstream_provider: Credential provider for the upstream connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/zones/{zone_id}/mcp-gateways/{application_id}/mcp-servers",
            body=await async_maybe_transform(
                {
                    "downstream": downstream,
                    "upstream": upstream,
                    "upstream_provider": upstream_provider,
                },
                mcp_gateway_create_mcp_server_params.McpGatewayCreateMcpServerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=McpGatewayCreateMcpServerResponse,
        )


class McpGatewaysResourceWithRawResponse:
    def __init__(self, mcp_gateways: McpGatewaysResource) -> None:
        self._mcp_gateways = mcp_gateways

        self.create_mcp_server = to_raw_response_wrapper(
            mcp_gateways.create_mcp_server,
        )


class AsyncMcpGatewaysResourceWithRawResponse:
    def __init__(self, mcp_gateways: AsyncMcpGatewaysResource) -> None:
        self._mcp_gateways = mcp_gateways

        self.create_mcp_server = async_to_raw_response_wrapper(
            mcp_gateways.create_mcp_server,
        )


class McpGatewaysResourceWithStreamingResponse:
    def __init__(self, mcp_gateways: McpGatewaysResource) -> None:
        self._mcp_gateways = mcp_gateways

        self.create_mcp_server = to_streamed_response_wrapper(
            mcp_gateways.create_mcp_server,
        )


class AsyncMcpGatewaysResourceWithStreamingResponse:
    def __init__(self, mcp_gateways: AsyncMcpGatewaysResource) -> None:
        self._mcp_gateways = mcp_gateways

        self.create_mcp_server = async_to_streamed_response_wrapper(
            mcp_gateways.create_mcp_server,
        )
