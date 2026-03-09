# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import McpGatewayCreateMcpServerResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mcp_server(self, client: KeycardAPI) -> None:
        mcp_gateway = client.zones.mcp_gateways.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mcp_server_with_all_params(self, client: KeycardAPI) -> None:
        mcp_gateway = client.zones.mcp_gateways.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={"slug": "slug"},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_mcp_server(self, client: KeycardAPI) -> None:
        response = client.zones.mcp_gateways.with_raw_response.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_gateway = response.parse()
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_mcp_server(self, client: KeycardAPI) -> None:
        with client.zones.mcp_gateways.with_streaming_response.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_gateway = response.parse()
            assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_mcp_server(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.mcp_gateways.with_raw_response.create_mcp_server(
                application_id="applicationId",
                zone_id="",
                downstream={},
                upstream={
                    "identifier": "x",
                    "name": "x",
                },
                upstream_provider={
                    "identifier": "x",
                    "name": "x",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.zones.mcp_gateways.with_raw_response.create_mcp_server(
                application_id="",
                zone_id="zoneId",
                downstream={},
                upstream={
                    "identifier": "x",
                    "name": "x",
                },
                upstream_provider={
                    "identifier": "x",
                    "name": "x",
                },
            )


class TestAsyncMcpGateways:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mcp_server(self, async_client: AsyncKeycardAPI) -> None:
        mcp_gateway = await async_client.zones.mcp_gateways.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mcp_server_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        mcp_gateway = await async_client.zones.mcp_gateways.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={"slug": "slug"},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_mcp_server(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.mcp_gateways.with_raw_response.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_gateway = await response.parse()
        assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_mcp_server(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.mcp_gateways.with_streaming_response.create_mcp_server(
            application_id="applicationId",
            zone_id="zoneId",
            downstream={},
            upstream={
                "identifier": "x",
                "name": "x",
            },
            upstream_provider={
                "identifier": "x",
                "name": "x",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_gateway = await response.parse()
            assert_matches_type(McpGatewayCreateMcpServerResponse, mcp_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_mcp_server(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.mcp_gateways.with_raw_response.create_mcp_server(
                application_id="applicationId",
                zone_id="",
                downstream={},
                upstream={
                    "identifier": "x",
                    "name": "x",
                },
                upstream_provider={
                    "identifier": "x",
                    "name": "x",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.zones.mcp_gateways.with_raw_response.create_mcp_server(
                application_id="",
                zone_id="zoneId",
                downstream={},
                upstream={
                    "identifier": "x",
                    "name": "x",
                },
                upstream_provider={
                    "identifier": "x",
                    "name": "x",
                },
            )
