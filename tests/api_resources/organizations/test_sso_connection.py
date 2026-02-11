# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.organizations import (
    SSOConnection,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSSOConnection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.retrieve(
            organization_id="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.retrieve(
            organization_id="x",
            expand=["permissions"],
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.organizations.sso_connection.with_raw_response.retrieve(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.organizations.sso_connection.with_streaming_response.retrieve(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.sso_connection.with_raw_response.retrieve(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.update(
            organization_id="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.update(
            organization_id="x",
            client_id="client_id",
            client_secret="client_secret",
            identifier="x",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.organizations.sso_connection.with_raw_response.update(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.organizations.sso_connection.with_streaming_response.update(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.sso_connection.with_raw_response.update(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disable(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.disable(
            organization_id="x",
        )
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disable_with_all_params(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.disable(
            organization_id="x",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: KeycardAPI) -> None:
        response = client.organizations.sso_connection.with_raw_response.disable(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = response.parse()
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: KeycardAPI) -> None:
        with client.organizations.sso_connection.with_streaming_response.disable(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = response.parse()
            assert sso_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.sso_connection.with_raw_response.disable(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enable(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enable_with_all_params(self, client: KeycardAPI) -> None:
        sso_connection = client.organizations.sso_connection.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
            client_secret="client_secret",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: KeycardAPI) -> None:
        response = client.organizations.sso_connection.with_raw_response.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: KeycardAPI) -> None:
        with client.organizations.sso_connection.with_streaming_response.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.sso_connection.with_raw_response.enable(
                organization_id="",
                client_id="client_id",
                identifier="x",
            )


class TestAsyncSSOConnection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.retrieve(
            organization_id="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.retrieve(
            organization_id="x",
            expand=["permissions"],
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.sso_connection.with_raw_response.retrieve(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = await response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.sso_connection.with_streaming_response.retrieve(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = await response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.sso_connection.with_raw_response.retrieve(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.update(
            organization_id="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.update(
            organization_id="x",
            client_id="client_id",
            client_secret="client_secret",
            identifier="x",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.sso_connection.with_raw_response.update(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = await response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.sso_connection.with_streaming_response.update(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = await response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.sso_connection.with_raw_response.update(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.disable(
            organization_id="x",
        )
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disable_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.disable(
            organization_id="x",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.sso_connection.with_raw_response.disable(
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = await response.parse()
        assert sso_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.sso_connection.with_streaming_response.disable(
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = await response.parse()
            assert sso_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.sso_connection.with_raw_response.disable(
                organization_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enable_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        sso_connection = await async_client.organizations.sso_connection.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
            client_secret="client_secret",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.sso_connection.with_raw_response.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_connection = await response.parse()
        assert_matches_type(SSOConnection, sso_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.sso_connection.with_streaming_response.enable(
            organization_id="x",
            client_id="client_id",
            identifier="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_connection = await response.parse()
            assert_matches_type(SSOConnection, sso_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.sso_connection.with_raw_response.enable(
                organization_id="",
                client_id="client_id",
                identifier="x",
            )
