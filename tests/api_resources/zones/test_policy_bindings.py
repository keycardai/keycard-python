# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api._utils import parse_datetime
from keycardai_api.types.zones import (
    PolicySetBinding,
    PolicyBindingListResponse,
    PolicyBindingRetrieveMetricsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyBindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.policy_bindings.with_raw_response.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = response.parse()
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.policy_bindings.with_streaming_response.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = response.parse()
            assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.retrieve(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.retrieve(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.list(
            zone_id="zone_id",
            filter_mode=["string"],
            filter_target_id=["string"],
            filter_target_type=["string"],
            mode="shadow",
            scope_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.policy_bindings.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = response.parse()
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.policy_bindings.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = response.parse()
            assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.delete(
            binding_id="binding_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.policy_bindings.with_raw_response.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = response.parse()
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.policy_bindings.with_streaming_response.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = response.parse()
            assert policy_binding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.delete(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.delete(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metrics(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metrics_with_all_params(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            psv_id="psv_id",
            scope="binding",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metrics(self, client: KeycardAPI) -> None:
        response = client.zones.policy_bindings.with_raw_response.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = response.parse()
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metrics(self, client: KeycardAPI) -> None:
        with client.zones.policy_bindings.with_streaming_response.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = response.parse()
            assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_metrics(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.retrieve_metrics(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.retrieve_metrics(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: KeycardAPI) -> None:
        policy_binding = client.zones.policy_bindings.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
            scope_target_id="scope_target_id",
            scope_type="zone",
            target_id="target_id",
            target_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: KeycardAPI) -> None:
        response = client.zones.policy_bindings.with_raw_response.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = response.parse()
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: KeycardAPI) -> None:
        with client.zones.policy_bindings.with_streaming_response.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = response.parse()
            assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_bindings.with_raw_response.set(
                zone_id="",
                mode="shadow",
                policy_set_id="policy_set_id",
                policy_set_version_id="policy_set_version_id",
            )


class TestAsyncPolicyBindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_bindings.with_raw_response.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = await response.parse()
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_bindings.with_streaming_response.retrieve(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = await response.parse()
            assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.retrieve(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.retrieve(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.list(
            zone_id="zone_id",
        )
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.list(
            zone_id="zone_id",
            filter_mode=["string"],
            filter_target_id=["string"],
            filter_target_type=["string"],
            mode="shadow",
            scope_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_bindings.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = await response.parse()
        assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_bindings.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = await response.parse()
            assert_matches_type(PolicyBindingListResponse, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.delete(
            binding_id="binding_id",
            zone_id="zone_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_bindings.with_raw_response.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = await response.parse()
        assert policy_binding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_bindings.with_streaming_response.delete(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = await response.parse()
            assert policy_binding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.delete(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.delete(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        )
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            psv_id="psv_id",
            scope="binding",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metrics(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_bindings.with_raw_response.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = await response.parse()
        assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metrics(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_bindings.with_streaming_response.retrieve_metrics(
            binding_id="binding_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = await response.parse()
            assert_matches_type(PolicyBindingRetrieveMetricsResponse, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_metrics(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.retrieve_metrics(
                binding_id="binding_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.retrieve_metrics(
                binding_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_binding = await async_client.zones.policy_bindings.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
            scope_target_id="scope_target_id",
            scope_type="zone",
            target_id="target_id",
            target_type="zone",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_bindings.with_raw_response.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_binding = await response.parse()
        assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_bindings.with_streaming_response.set(
            zone_id="zone_id",
            mode="shadow",
            policy_set_id="policy_set_id",
            policy_set_version_id="policy_set_version_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_binding = await response.parse()
            assert_matches_type(PolicySetBinding, policy_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_bindings.with_raw_response.set(
                zone_id="",
                mode="shadow",
                policy_set_id="policy_set_id",
                policy_set_version_id="policy_set_version_id",
            )
