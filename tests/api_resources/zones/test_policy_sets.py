# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import (
    PolicySetWithBinding,
    PolicySetListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicySets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.create(
            zone_id="zone_id",
            name="name",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.create(
            zone_id="zone_id",
            name="name",
            scope_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.with_raw_response.create(
            zone_id="zone_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.with_streaming_response.create(
            zone_id="zone_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.with_raw_response.create(
                zone_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.with_raw_response.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.with_streaming_response.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.with_raw_response.retrieve(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.with_raw_response.retrieve(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            name="name",
            if_match="If-Match",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.with_raw_response.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.with_streaming_response.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.with_raw_response.update(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.with_raw_response.update(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.list(
            zone_id="zone_id",
            active=True,
            after="x",
            before="x",
            expand=["total_count"],
            filter_active=True,
            filter_owner_type=["string"],
            filter_scope_type=["string"],
            limit=1,
            order="asc",
            query=["x"],
            query_name=["x"],
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: KeycardAPI) -> None:
        policy_set = client.zones.policy_sets.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            if_match="If-Match",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.with_raw_response.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.with_streaming_response.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.with_raw_response.archive(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.with_raw_response.archive(
                policy_set_id="",
                zone_id="zone_id",
            )


class TestAsyncPolicySets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.create(
            zone_id="zone_id",
            name="name",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.create(
            zone_id="zone_id",
            name="name",
            scope_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.with_raw_response.create(
            zone_id="zone_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.with_streaming_response.create(
            zone_id="zone_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.create(
                zone_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.with_raw_response.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.with_streaming_response.retrieve(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.retrieve(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.retrieve(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            name="name",
            if_match="If-Match",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.with_raw_response.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.with_streaming_response.update(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.update(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.update(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.list(
            zone_id="zone_id",
            active=True,
            after="x",
            before="x",
            expand=["total_count"],
            filter_active=True,
            filter_owner_type=["string"],
            filter_scope_type=["string"],
            limit=1,
            order="asc",
            query=["x"],
            query_name=["x"],
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetListResponse, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_set = await async_client.zones.policy_sets.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            if_match="If-Match",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.with_raw_response.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_set = await response.parse()
        assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.with_streaming_response.archive(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_set = await response.parse()
            assert_matches_type(PolicySetWithBinding, policy_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.archive(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.with_raw_response.archive(
                policy_set_id="",
                zone_id="zone_id",
            )
