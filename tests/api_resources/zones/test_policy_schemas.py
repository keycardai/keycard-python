# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import (
    PolicySchemaListResponse,
    SchemaVersionWithZoneInfo,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicySchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.retrieve(
            version="version",
            zone_id="zone_id",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.retrieve(
            version="version",
            zone_id="zone_id",
            format="cedar",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.policy_schemas.with_raw_response.retrieve(
            version="version",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = response.parse()
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.policy_schemas.with_streaming_response.retrieve(
            version="version",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = response.parse()
            assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_schemas.with_raw_response.retrieve(
                version="version",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.zones.policy_schemas.with_raw_response.retrieve(
                version="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.list(
            zone_id="zone_id",
            after="after",
            before="before",
            expand=["total_count"],
            format="cedar",
            is_default=True,
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.policy_schemas.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = response.parse()
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.policy_schemas.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = response.parse()
            assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_schemas.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_default(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.set_default(
            version="version",
            zone_id="zone_id",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_default_with_all_params(self, client: KeycardAPI) -> None:
        policy_schema = client.zones.policy_schemas.set_default(
            version="version",
            zone_id="zone_id",
            body={},
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_default(self, client: KeycardAPI) -> None:
        response = client.zones.policy_schemas.with_raw_response.set_default(
            version="version",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = response.parse()
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_default(self, client: KeycardAPI) -> None:
        with client.zones.policy_schemas.with_streaming_response.set_default(
            version="version",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = response.parse()
            assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_default(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_schemas.with_raw_response.set_default(
                version="version",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.zones.policy_schemas.with_raw_response.set_default(
                version="",
                zone_id="zone_id",
            )


class TestAsyncPolicySchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.retrieve(
            version="version",
            zone_id="zone_id",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.retrieve(
            version="version",
            zone_id="zone_id",
            format="cedar",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_schemas.with_raw_response.retrieve(
            version="version",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = await response.parse()
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_schemas.with_streaming_response.retrieve(
            version="version",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = await response.parse()
            assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_schemas.with_raw_response.retrieve(
                version="version",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.zones.policy_schemas.with_raw_response.retrieve(
                version="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.list(
            zone_id="zone_id",
            after="after",
            before="before",
            expand=["total_count"],
            format="cedar",
            is_default=True,
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_schemas.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = await response.parse()
        assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_schemas.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = await response.parse()
            assert_matches_type(PolicySchemaListResponse, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_schemas.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_default(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.set_default(
            version="version",
            zone_id="zone_id",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_default_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_schema = await async_client.zones.policy_schemas.set_default(
            version="version",
            zone_id="zone_id",
            body={},
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_default(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_schemas.with_raw_response.set_default(
            version="version",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_schema = await response.parse()
        assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_default(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_schemas.with_streaming_response.set_default(
            version="version",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_schema = await response.parse()
            assert_matches_type(SchemaVersionWithZoneInfo, policy_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_default(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_schemas.with_raw_response.set_default(
                version="version",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.zones.policy_schemas.with_raw_response.set_default(
                version="",
                zone_id="zone_id",
            )
