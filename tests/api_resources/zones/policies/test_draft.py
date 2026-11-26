# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import PolicyDraft

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
            expand="user",
            format="cedar",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.policies.draft.with_raw_response.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.policies.draft.with_streaming_response.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PolicyDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policies.draft.with_raw_response.retrieve(
                policy_id="policy_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zones.policies.draft.with_raw_response.retrieve(
                policy_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.delete(
            policy_id="policy_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.policies.draft.with_raw_response.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.policies.draft.with_streaming_response.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policies.draft.with_raw_response.delete(
                policy_id="policy_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zones.policies.draft.with_raw_response.delete(
                policy_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KeycardAPI) -> None:
        draft = client.zones.policies.draft.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
            format="cedar",
            validate_cedar=True,
            cedar_json={},
            cedar_raw="cedar_raw",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KeycardAPI) -> None:
        response = client.zones.policies.draft.with_raw_response.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KeycardAPI) -> None:
        with client.zones.policies.draft.with_streaming_response.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PolicyDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policies.draft.with_raw_response.upsert(
                policy_id="policy_id",
                zone_id="",
                schema_version="schema_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zones.policies.draft.with_raw_response.upsert(
                policy_id="",
                zone_id="zone_id",
                schema_version="schema_version",
            )


class TestAsyncDraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
            expand="user",
            format="cedar",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policies.draft.with_raw_response.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policies.draft.with_streaming_response.retrieve(
            policy_id="policy_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PolicyDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.retrieve(
                policy_id="policy_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.retrieve(
                policy_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.delete(
            policy_id="policy_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policies.draft.with_raw_response.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policies.draft.with_streaming_response.delete(
            policy_id="policy_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.delete(
                policy_id="policy_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.delete(
                policy_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        draft = await async_client.zones.policies.draft.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
            format="cedar",
            validate_cedar=True,
            cedar_json={},
            cedar_raw="cedar_raw",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policies.draft.with_raw_response.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(PolicyDraft, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policies.draft.with_streaming_response.upsert(
            policy_id="policy_id",
            zone_id="zone_id",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PolicyDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.upsert(
                policy_id="policy_id",
                zone_id="",
                schema_version="schema_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zones.policies.draft.with_raw_response.upsert(
                policy_id="",
                zone_id="zone_id",
                schema_version="schema_version",
            )
