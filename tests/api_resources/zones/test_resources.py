# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.zones import (
    ResourceListResponse,
)
from keycard_api.types.zones.applications import Resource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
            application_id="application_id",
            credential_provider_id="credential_provider_id",
            description="description",
            metadata={"docs_url": "https://example.com"},
            scopes=["string"],
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.resources.with_raw_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.resources.with_streaming_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.resources.with_raw_response.create(
                zone_id="",
                identifier="x",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.resources.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.resources.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.resources.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.resources.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.update(
            id="id",
            zone_id="zoneId",
            application_id="application_id",
            credential_provider_id="credential_provider_id",
            description="description",
            identifier="x",
            metadata={"docs_url": "https://example.com"},
            name="x",
            scopes=["x"],
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.zones.resources.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.zones.resources.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.resources.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.resources.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.list(
            zone_id="zoneId",
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.list(
            zone_id="zoneId",
            after="x",
            before="x",
            credential_provider_id="credentialProviderId",
            expand="total_count",
            identifier="identifier",
            limit=1,
            slug="slug",
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.resources.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.resources.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(ResourceListResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.resources.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        resource = client.zones.resources.delete(
            id="id",
            zone_id="zoneId",
        )
        assert resource is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.resources.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert resource is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.resources.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.resources.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.resources.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )


class TestAsyncResources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
            application_id="application_id",
            credential_provider_id="credential_provider_id",
            description="description",
            metadata={"docs_url": "https://example.com"},
            scopes=["string"],
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.resources.with_raw_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.resources.with_streaming_response.create(
            zone_id="zoneId",
            identifier="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.resources.with_raw_response.create(
                zone_id="",
                identifier="x",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.resources.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.resources.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.resources.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.resources.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.update(
            id="id",
            zone_id="zoneId",
            application_id="application_id",
            credential_provider_id="credential_provider_id",
            description="description",
            identifier="x",
            metadata={"docs_url": "https://example.com"},
            name="x",
            scopes=["x"],
        )
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.resources.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(Resource, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.resources.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(Resource, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.resources.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.resources.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.list(
            zone_id="zoneId",
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.list(
            zone_id="zoneId",
            after="x",
            before="x",
            credential_provider_id="credentialProviderId",
            expand="total_count",
            identifier="identifier",
            limit=1,
            slug="slug",
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.resources.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.resources.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(ResourceListResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.resources.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        resource = await async_client.zones.resources.delete(
            id="id",
            zone_id="zoneId",
        )
        assert resource is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.resources.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert resource is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.resources.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.resources.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.resources.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )
