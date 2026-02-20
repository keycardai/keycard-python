# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.zones import (
    Grant,
    DelegatedGrantListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDelegatedGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        delegated_grant = client.zones.delegated_grants.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.delegated_grants.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = response.parse()
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.delegated_grants.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = response.parse()
            assert_matches_type(Grant, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.delegated_grants.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.delegated_grants.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        delegated_grant = client.zones.delegated_grants.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        )
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.zones.delegated_grants.with_raw_response.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = response.parse()
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.zones.delegated_grants.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = response.parse()
            assert_matches_type(Grant, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.delegated_grants.with_raw_response.update(
                id="id",
                zone_id="",
                status="revoked",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.delegated_grants.with_raw_response.update(
                id="",
                zone_id="zoneId",
                status="revoked",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        delegated_grant = client.zones.delegated_grants.list(
            zone_id="zoneId",
        )
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        delegated_grant = client.zones.delegated_grants.list(
            zone_id="zoneId",
            active="true",
            after="x",
            before="x",
            expand="total_count",
            limit=1,
            resource_id="resource_id",
            status="active",
            user_id="user_id",
        )
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.delegated_grants.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = response.parse()
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.delegated_grants.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = response.parse()
            assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.delegated_grants.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        delegated_grant = client.zones.delegated_grants.delete(
            id="id",
            zone_id="zoneId",
        )
        assert delegated_grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.delegated_grants.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = response.parse()
        assert delegated_grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.delegated_grants.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = response.parse()
            assert delegated_grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.delegated_grants.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.delegated_grants.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )


class TestAsyncDelegatedGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        delegated_grant = await async_client.zones.delegated_grants.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.delegated_grants.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = await response.parse()
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.delegated_grants.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = await response.parse()
            assert_matches_type(Grant, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        delegated_grant = await async_client.zones.delegated_grants.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        )
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.delegated_grants.with_raw_response.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = await response.parse()
        assert_matches_type(Grant, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.delegated_grants.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
            status="revoked",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = await response.parse()
            assert_matches_type(Grant, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.update(
                id="id",
                zone_id="",
                status="revoked",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.update(
                id="",
                zone_id="zoneId",
                status="revoked",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        delegated_grant = await async_client.zones.delegated_grants.list(
            zone_id="zoneId",
        )
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        delegated_grant = await async_client.zones.delegated_grants.list(
            zone_id="zoneId",
            active="true",
            after="x",
            before="x",
            expand="total_count",
            limit=1,
            resource_id="resource_id",
            status="active",
            user_id="user_id",
        )
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.delegated_grants.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = await response.parse()
        assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.delegated_grants.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = await response.parse()
            assert_matches_type(DelegatedGrantListResponse, delegated_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        delegated_grant = await async_client.zones.delegated_grants.delete(
            id="id",
            zone_id="zoneId",
        )
        assert delegated_grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.delegated_grants.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegated_grant = await response.parse()
        assert delegated_grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.delegated_grants.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegated_grant = await response.parse()
            assert delegated_grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.delegated_grants.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )
