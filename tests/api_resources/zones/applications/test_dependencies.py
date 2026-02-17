# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.zones.applications import (
    Resource,
    DependencyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDependencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert_matches_type(Resource, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.applications.dependencies.with_raw_response.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = response.parse()
        assert_matches_type(Resource, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.applications.dependencies.with_streaming_response.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = response.parse()
            assert_matches_type(Resource, dependency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.list(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.list(
            id="id",
            zone_id="zoneId",
            after="x",
            before="x",
            cursor="cursor",
            expand="total_count",
            limit=1,
            when_accessing="when_accessing",
        )
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.applications.dependencies.with_raw_response.list(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = response.parse()
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.applications.dependencies.with_streaming_response.list(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = response.parse()
            assert_matches_type(DependencyListResponse, dependency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.list(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.list(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
            when_accessing=["string"],
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: KeycardAPI) -> None:
        response = client.zones.applications.dependencies.with_raw_response.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = response.parse()
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: KeycardAPI) -> None:
        with client.zones.applications.dependencies.with_streaming_response.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = response.parse()
            assert dependency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: KeycardAPI) -> None:
        dependency = client.zones.applications.dependencies.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: KeycardAPI) -> None:
        response = client.zones.applications.dependencies.with_raw_response.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = response.parse()
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: KeycardAPI) -> None:
        with client.zones.applications.dependencies.with_streaming_response.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = response.parse()
            assert dependency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )


class TestAsyncDependencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert_matches_type(Resource, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.dependencies.with_raw_response.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = await response.parse()
        assert_matches_type(Resource, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.dependencies.with_streaming_response.retrieve(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = await response.parse()
            assert_matches_type(Resource, dependency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.retrieve(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.list(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.list(
            id="id",
            zone_id="zoneId",
            after="x",
            before="x",
            cursor="cursor",
            expand="total_count",
            limit=1,
            when_accessing="when_accessing",
        )
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.dependencies.with_raw_response.list(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = await response.parse()
        assert_matches_type(DependencyListResponse, dependency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.dependencies.with_streaming_response.list(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = await response.parse()
            assert_matches_type(DependencyListResponse, dependency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.list(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.list(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
            when_accessing=["string"],
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.dependencies.with_raw_response.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = await response.parse()
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.dependencies.with_streaming_response.add(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = await response.parse()
            assert dependency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.add(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncKeycardAPI) -> None:
        dependency = await async_client.zones.applications.dependencies.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.dependencies.with_raw_response.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependency = await response.parse()
        assert dependency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.dependencies.with_streaming_response.remove(
            dependency_id="dependencyId",
            zone_id="zoneId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependency = await response.parse()
            assert dependency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="dependencyId",
                zone_id="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="dependencyId",
                zone_id="zoneId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependency_id` but received ''"):
            await async_client.zones.applications.dependencies.with_raw_response.remove(
                dependency_id="",
                zone_id="zoneId",
                id="id",
            )
