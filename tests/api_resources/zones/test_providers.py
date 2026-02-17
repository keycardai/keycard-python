# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.zones import (
    Provider,
    ProviderListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
            client_id="client_id",
            client_secret="client_secret",
            description="description",
            metadata={},
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "authorization_resource_enabled": True,
                    "authorization_resource_parameter": "authorization_resource_parameter",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scope_parameter": "scope_parameter",
                    "scope_separator": "scope_separator",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                    "token_response_access_token_pointer": "token_response_access_token_pointer",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.providers.with_raw_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.providers.with_streaming_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.providers.with_raw_response.create(
                zone_id="",
                identifier="x",
                name="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.providers.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.providers.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.providers.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.providers.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.update(
            id="id",
            zone_id="zoneId",
            client_id="client_id",
            client_secret="client_secret",
            description="description",
            identifier="x",
            metadata={},
            name="x",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "authorization_resource_enabled": True,
                    "authorization_resource_parameter": "authorization_resource_parameter",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scope_parameter": "scope_parameter",
                    "scope_separator": "scope_separator",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                    "token_response_access_token_pointer": "token_response_access_token_pointer",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.zones.providers.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.zones.providers.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.providers.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.providers.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.list(
            zone_id="zoneId",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.list(
            zone_id="zoneId",
            cursor="cursor",
            identifier="identifier",
            limit=1,
            slug="slug",
            type="external",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.providers.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.providers.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.providers.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        provider = client.zones.providers.delete(
            id="id",
            zone_id="zoneId",
        )
        assert provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.providers.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.providers.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert provider is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.providers.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.providers.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )


class TestAsyncProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
            client_id="client_id",
            client_secret="client_secret",
            description="description",
            metadata={},
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "authorization_resource_enabled": True,
                    "authorization_resource_parameter": "authorization_resource_parameter",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scope_parameter": "scope_parameter",
                    "scope_separator": "scope_separator",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                    "token_response_access_token_pointer": "token_response_access_token_pointer",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.providers.with_raw_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.providers.with_streaming_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.providers.with_raw_response.create(
                zone_id="",
                identifier="x",
                name="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.providers.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.providers.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.providers.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.providers.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.update(
            id="id",
            zone_id="zoneId",
            client_id="client_id",
            client_secret="client_secret",
            description="description",
            identifier="x",
            metadata={},
            name="x",
            protocols={
                "oauth2": {
                    "authorization_endpoint": "https://example.com",
                    "authorization_resource_enabled": True,
                    "authorization_resource_parameter": "authorization_resource_parameter",
                    "code_challenge_methods_supported": ["string"],
                    "jwks_uri": "https://example.com",
                    "registration_endpoint": "https://example.com",
                    "scope_parameter": "scope_parameter",
                    "scope_separator": "scope_separator",
                    "scopes_supported": ["string"],
                    "token_endpoint": "https://example.com",
                    "token_response_access_token_pointer": "token_response_access_token_pointer",
                },
                "openid": {"userinfo_endpoint": "https://example.com"},
            },
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.providers.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.providers.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.providers.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.providers.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.list(
            zone_id="zoneId",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.list(
            zone_id="zoneId",
            cursor="cursor",
            identifier="identifier",
            limit=1,
            slug="slug",
            type="external",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.providers.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.providers.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.providers.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        provider = await async_client.zones.providers.delete(
            id="id",
            zone_id="zoneId",
        )
        assert provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.providers.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.providers.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert provider is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.providers.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.providers.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )
