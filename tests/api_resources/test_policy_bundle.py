# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyBundle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = client.policy_bundle.retrieve()
        assert policy_bundle.is_closed
        assert policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_with_all_params(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = client.policy_bundle.retrieve(
            if_none_match="If-None-Match",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle.is_closed
        assert policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        policy_bundle = client.policy_bundle.with_raw_response.retrieve()

        assert policy_bundle.is_closed is True
        assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"
        assert policy_bundle.json() == {"foo": "bar"}
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.policy_bundle.with_streaming_response.retrieve() as policy_bundle:
            assert not policy_bundle.is_closed
            assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"

            assert policy_bundle.json() == {"foo": "bar"}
            assert cast(Any, policy_bundle.is_closed) is True
            assert isinstance(policy_bundle, StreamedBinaryAPIResponse)

        assert cast(Any, policy_bundle.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = client.policy_bundle.update(
            body=b"Example data",
        )
        assert policy_bundle.is_closed
        assert policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = client.policy_bundle.update(
            body=b"Example data",
            if_match="If-Match",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle.is_closed
        assert policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        policy_bundle = client.policy_bundle.with_raw_response.update(
            body=b"Example data",
        )

        assert policy_bundle.is_closed is True
        assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"
        assert policy_bundle.json() == {"foo": "bar"}
        assert isinstance(policy_bundle, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: KeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.policy_bundle.with_streaming_response.update(
            body=b"Example data",
        ) as policy_bundle:
            assert not policy_bundle.is_closed
            assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"

            assert policy_bundle.json() == {"foo": "bar"}
            assert cast(Any, policy_bundle.is_closed) is True
            assert isinstance(policy_bundle, StreamedBinaryAPIResponse)

        assert cast(Any, policy_bundle.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset(self, client: KeycardAPI) -> None:
        policy_bundle = client.policy_bundle.reset()
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_with_all_params(self, client: KeycardAPI) -> None:
        policy_bundle = client.policy_bundle.reset(
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: KeycardAPI) -> None:
        response = client.policy_bundle.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_bundle = response.parse()
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: KeycardAPI) -> None:
        with client.policy_bundle.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_bundle = response.parse()
            assert policy_bundle is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicyBundle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = await async_client.policy_bundle.retrieve()
        assert policy_bundle.is_closed
        assert await policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = await async_client.policy_bundle.retrieve(
            if_none_match="If-None-Match",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle.is_closed
        assert await policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        policy_bundle = await async_client.policy_bundle.with_raw_response.retrieve()

        assert policy_bundle.is_closed is True
        assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await policy_bundle.json() == {"foo": "bar"}
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.get("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.policy_bundle.with_streaming_response.retrieve() as policy_bundle:
            assert not policy_bundle.is_closed
            assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await policy_bundle.json() == {"foo": "bar"}
            assert cast(Any, policy_bundle.is_closed) is True
            assert isinstance(policy_bundle, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, policy_bundle.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = await async_client.policy_bundle.update(
            body=b"Example data",
        )
        assert policy_bundle.is_closed
        assert await policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        policy_bundle = await async_client.policy_bundle.update(
            body=b"Example data",
            if_match="If-Match",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle.is_closed
        assert await policy_bundle.json() == {"foo": "bar"}
        assert cast(Any, policy_bundle.is_closed) is True
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        policy_bundle = await async_client.policy_bundle.with_raw_response.update(
            body=b"Example data",
        )

        assert policy_bundle.is_closed is True
        assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await policy_bundle.json() == {"foo": "bar"}
        assert isinstance(policy_bundle, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI, respx_mock: MockRouter) -> None:
        respx_mock.put("/policy/bundle").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.policy_bundle.with_streaming_response.update(
            body=b"Example data",
        ) as policy_bundle:
            assert not policy_bundle.is_closed
            assert policy_bundle.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await policy_bundle.json() == {"foo": "bar"}
            assert cast(Any, policy_bundle.is_closed) is True
            assert isinstance(policy_bundle, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, policy_bundle.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncKeycardAPI) -> None:
        policy_bundle = await async_client.policy_bundle.reset()
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_bundle = await async_client.policy_bundle.reset(
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.policy_bundle.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_bundle = await response.parse()
        assert policy_bundle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.policy_bundle.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_bundle = await response.parse()
            assert policy_bundle is None

        assert cast(Any, response.is_closed) is True
