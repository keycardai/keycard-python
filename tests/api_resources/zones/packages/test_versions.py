# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones.packages import PackageVersion, PackageVersionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        version = client.zones.packages.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        )
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.packages.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.packages.versions.with_raw_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.packages.versions.with_streaming_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PackageVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.packages.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="",
                package_id="lkfwmkifjr:4mtu9913w4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.zones.packages.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="zone_id",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.zones.packages.versions.with_raw_response.retrieve(
                version_id="",
                zone_id="zone_id",
                package_id="lkfwmkifjr:4mtu9913w4",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        version = client.zones.packages.versions.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.packages.versions.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
            after="x",
            before="x",
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.packages.versions.with_raw_response.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.packages.versions.with_streaming_response.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PackageVersionList, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.packages.versions.with_raw_response.list(
                package_id="lkfwmkifjr:4mtu9913w4",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.zones.packages.versions.with_raw_response.list(
                package_id="",
                zone_id="zone_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.packages.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        )
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.packages.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.packages.versions.with_raw_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PackageVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.packages.versions.with_streaming_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            package_id="lkfwmkifjr:4mtu9913w4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PackageVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.packages.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="",
                package_id="lkfwmkifjr:4mtu9913w4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.zones.packages.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="zone_id",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.zones.packages.versions.with_raw_response.retrieve(
                version_id="",
                zone_id="zone_id",
                package_id="lkfwmkifjr:4mtu9913w4",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.packages.versions.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.packages.versions.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
            after="x",
            before="x",
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.packages.versions.with_raw_response.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PackageVersionList, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.packages.versions.with_streaming_response.list(
            package_id="lkfwmkifjr:4mtu9913w4",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PackageVersionList, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.packages.versions.with_raw_response.list(
                package_id="lkfwmkifjr:4mtu9913w4",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.zones.packages.versions.with_raw_response.list(
                package_id="",
                zone_id="zone_id",
            )
