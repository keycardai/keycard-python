# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import Task, Install, InstallList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        install = client.zones.installs.create(
            zone_id="zone_id",
            package_id="package_id",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        install = client.zones.installs.create(
            zone_id="zone_id",
            package_id="package_id",
            inputs={"foo": "bar"},
            version=0,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.installs.with_raw_response.create(
            zone_id="zone_id",
            package_id="package_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = response.parse()
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.installs.with_streaming_response.create(
            zone_id="zone_id",
            package_id="package_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = response.parse()
            assert_matches_type(Task, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.installs.with_raw_response.create(
                zone_id="",
                package_id="package_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        install = client.zones.installs.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        )
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        install = client.zones.installs.retrieve(
            install_id="install_id",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.installs.with_raw_response.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = response.parse()
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.installs.with_streaming_response.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = response.parse()
            assert_matches_type(Install, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.installs.with_raw_response.retrieve(
                install_id="install_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `install_id` but received ''"):
            client.zones.installs.with_raw_response.retrieve(
                install_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        install = client.zones.installs.list(
            zone_id="zone_id",
        )
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        install = client.zones.installs.list(
            zone_id="zone_id",
            after="x",
            before="x",
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.installs.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = response.parse()
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.installs.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = response.parse()
            assert_matches_type(InstallList, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.installs.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        install = client.zones.installs.delete(
            install_id="install_id",
            zone_id="zone_id",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: KeycardAPI) -> None:
        install = client.zones.installs.delete(
            install_id="install_id",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.installs.with_raw_response.delete(
            install_id="install_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = response.parse()
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.installs.with_streaming_response.delete(
            install_id="install_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = response.parse()
            assert_matches_type(Task, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.installs.with_raw_response.delete(
                install_id="install_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `install_id` but received ''"):
            client.zones.installs.with_raw_response.delete(
                install_id="",
                zone_id="zone_id",
            )


class TestAsyncInstalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.create(
            zone_id="zone_id",
            package_id="package_id",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.create(
            zone_id="zone_id",
            package_id="package_id",
            inputs={"foo": "bar"},
            version=0,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.installs.with_raw_response.create(
            zone_id="zone_id",
            package_id="package_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = await response.parse()
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.installs.with_streaming_response.create(
            zone_id="zone_id",
            package_id="package_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = await response.parse()
            assert_matches_type(Task, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.installs.with_raw_response.create(
                zone_id="",
                package_id="package_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        )
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.retrieve(
            install_id="install_id",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.installs.with_raw_response.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = await response.parse()
        assert_matches_type(Install, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.installs.with_streaming_response.retrieve(
            install_id="install_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = await response.parse()
            assert_matches_type(Install, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.installs.with_raw_response.retrieve(
                install_id="install_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `install_id` but received ''"):
            await async_client.zones.installs.with_raw_response.retrieve(
                install_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.list(
            zone_id="zone_id",
        )
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.list(
            zone_id="zone_id",
            after="x",
            before="x",
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.installs.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = await response.parse()
        assert_matches_type(InstallList, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.installs.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = await response.parse()
            assert_matches_type(InstallList, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.installs.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.delete(
            install_id="install_id",
            zone_id="zone_id",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        install = await async_client.zones.installs.delete(
            install_id="install_id",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.installs.with_raw_response.delete(
            install_id="install_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = await response.parse()
        assert_matches_type(Task, install, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.installs.with_streaming_response.delete(
            install_id="install_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = await response.parse()
            assert_matches_type(Task, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.installs.with_raw_response.delete(
                install_id="install_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `install_id` but received ''"):
            await async_client.zones.installs.with_raw_response.delete(
                install_id="",
                zone_id="zone_id",
            )
