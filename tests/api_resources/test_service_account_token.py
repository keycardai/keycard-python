# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types import ServiceAccountTokenCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceAccountToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        service_account_token = client.service_account_token.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        )
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        service_account_token = client.service_account_token.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.service_account_token.with_raw_response.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account_token = response.parse()
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.service_account_token.with_streaming_response.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account_token = response.parse()
            assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServiceAccountToken:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        service_account_token = await async_client.service_account_token.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        )
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        service_account_token = await async_client.service_account_token.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.service_account_token.with_raw_response.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account_token = await response.parse()
        assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.service_account_token.with_streaming_response.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account_token = await response.parse()
            assert_matches_type(ServiceAccountTokenCreateResponse, service_account_token, path=["response"])

        assert cast(Any, response.is_closed) is True
