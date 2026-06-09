# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import Package

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPackages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        package = client.zones.packages.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        package = client.zones.packages.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.packages.with_raw_response.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.packages.with_streaming_response.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(Package, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.packages.with_raw_response.retrieve(
                package_id="lkfwmkifjr:4mtu9913w4",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.zones.packages.with_raw_response.retrieve(
                package_id="",
                zone_id="zone_id",
            )


class TestAsyncPackages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        package = await async_client.zones.packages.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        package = await async_client.zones.packages.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.packages.with_raw_response.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(Package, package, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.packages.with_streaming_response.retrieve(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(Package, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.packages.with_raw_response.retrieve(
                package_id="lkfwmkifjr:4mtu9913w4",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.zones.packages.with_raw_response.retrieve(
                package_id="",
                zone_id="zone_id",
            )
