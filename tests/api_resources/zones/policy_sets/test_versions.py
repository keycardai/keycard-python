# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones.policy_sets import (
    PolicySetVersion,
    VersionListResponse,
    VersionListPoliciesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                        "sha": "sha",
                    }
                ]
            },
            schema_version="schema_version",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.create(
                policy_set_id="policy_set_id",
                zone_id="",
                manifest={
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                        }
                    ]
                },
                schema_version="schema_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.create(
                policy_set_id="",
                zone_id="zone_id",
                manifest={
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                        }
                    ]
                },
                schema_version="schema_version",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.update(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
                active=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.update(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
                active=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.update(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
                active=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            after="x",
            before="x",
            expand=["total_count"],
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.list(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.list(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_policies(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_policies_with_all_params(self, client: KeycardAPI) -> None:
        version = client.zones.policy_sets.versions.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            after="x",
            before="x",
            expand=["total_count"],
            format="cedar",
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_policies(self, client: KeycardAPI) -> None:
        response = client.zones.policy_sets.versions.with_raw_response.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_policies(self, client: KeycardAPI) -> None:
        with client.zones.policy_sets.versions.with_streaming_response.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_policies(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                        "sha": "sha",
                    }
                ]
            },
            schema_version="schema_version",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.create(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            manifest={
                "entries": [
                    {
                        "policy_id": "policy_id",
                        "policy_version_id": "policy_version_id",
                    }
                ]
            },
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.create(
                policy_set_id="policy_set_id",
                zone_id="",
                manifest={
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                        }
                    ]
                },
                schema_version="schema_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.create(
                policy_set_id="",
                zone_id="zone_id",
                manifest={
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                        }
                    ]
                },
                schema_version="schema_version",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.retrieve(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.retrieve(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.update(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.update(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
                active=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.update(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
                active=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.update(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
                active=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
            after="x",
            before="x",
            expand=["total_count"],
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.list(
            policy_set_id="policy_set_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.list(
                policy_set_id="policy_set_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.list(
                policy_set_id="",
                zone_id="zone_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(PolicySetVersion, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.archive(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(PolicySetVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.archive(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_policies(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_policies_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        version = await async_client.zones.policy_sets.versions.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
            after="x",
            before="x",
            expand=["total_count"],
            format="cedar",
            limit=1,
            order="asc",
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_policies(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_sets.versions.with_raw_response.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_policies(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_sets.versions.with_streaming_response.list_policies(
            version_id="version_id",
            zone_id="zone_id",
            policy_set_id="policy_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionListPoliciesResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_policies(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="version_id",
                zone_id="",
                policy_set_id="policy_set_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_set_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="version_id",
                zone_id="zone_id",
                policy_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.zones.policy_sets.versions.with_raw_response.list_policies(
                version_id="",
                zone_id="zone_id",
                policy_set_id="policy_set_id",
            )
