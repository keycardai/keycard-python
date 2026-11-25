# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import PolicyValidationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        policy_validation = client.zones.policy_validations.create(
            zone_id="zone_id",
            schema_version="schema_version",
        )
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        policy_validation = client.zones.policy_validations.create(
            zone_id="zone_id",
            schema_version="schema_version",
            cedar_json={},
            cedar_raw="cedar_raw",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.policy_validations.with_raw_response.create(
            zone_id="zone_id",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_validation = response.parse()
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.policy_validations.with_streaming_response.create(
            zone_id="zone_id",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_validation = response.parse()
            assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_validations.with_raw_response.create(
                zone_id="",
                schema_version="schema_version",
            )


class TestAsyncPolicyValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        policy_validation = await async_client.zones.policy_validations.create(
            zone_id="zone_id",
            schema_version="schema_version",
        )
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_validation = await async_client.zones.policy_validations.create(
            zone_id="zone_id",
            schema_version="schema_version",
            cedar_json={},
            cedar_raw="cedar_raw",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_validations.with_raw_response.create(
            zone_id="zone_id",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_validation = await response.parse()
        assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_validations.with_streaming_response.create(
            zone_id="zone_id",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_validation = await response.parse()
            assert_matches_type(PolicyValidationCreateResponse, policy_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_validations.with_raw_response.create(
                zone_id="",
                schema_version="schema_version",
            )
