# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones.users import RoleAssignment
from keycardai_api.types.zones.applications import (
    RoleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.list(
            application_id="applicationId",
            zone_id="zoneId",
        )
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.list(
            application_id="applicationId",
            zone_id="zoneId",
            after="x",
            before="x",
            expand="total_count",
            limit=1,
        )
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.applications.roles.with_raw_response.list(
            application_id="applicationId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.applications.roles.with_streaming_response.list(
            application_id="applicationId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(RoleListResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.roles.with_raw_response.list(
                application_id="applicationId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.zones.applications.roles.with_raw_response.list(
                application_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.assign(
            application_id="applicationId",
            zone_id="zoneId",
        )
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign_with_all_params(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.assign(
            application_id="applicationId",
            zone_id="zoneId",
            owner_type="platform",
            role_id="role_id",
            role_identifier="role_identifier",
            scope_id="x",
            scope_type="x",
        )
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: KeycardAPI) -> None:
        response = client.zones.applications.roles.with_raw_response.assign(
            application_id="applicationId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: KeycardAPI) -> None:
        with client.zones.applications.roles.with_streaming_response.assign(
            application_id="applicationId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(RoleAssignment, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.roles.with_raw_response.assign(
                application_id="applicationId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.zones.applications.roles.with_raw_response.assign(
                application_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        )
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_with_all_params(self, client: KeycardAPI) -> None:
        role = client.zones.applications.roles.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
            scope_id="x",
            scope_type="x",
        )
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: KeycardAPI) -> None:
        response = client.zones.applications.roles.with_raw_response.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: KeycardAPI) -> None:
        with client.zones.applications.roles.with_streaming_response.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert role is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.applications.roles.with_raw_response.revoke(
                role_id="roleId",
                zone_id="",
                application_id="applicationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.zones.applications.roles.with_raw_response.revoke(
                role_id="roleId",
                zone_id="zoneId",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.zones.applications.roles.with_raw_response.revoke(
                role_id="",
                zone_id="zoneId",
                application_id="applicationId",
            )


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.list(
            application_id="applicationId",
            zone_id="zoneId",
        )
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.list(
            application_id="applicationId",
            zone_id="zoneId",
            after="x",
            before="x",
            expand="total_count",
            limit=1,
        )
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.roles.with_raw_response.list(
            application_id="applicationId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.roles.with_streaming_response.list(
            application_id="applicationId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(RoleListResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.list(
                application_id="applicationId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.list(
                application_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.assign(
            application_id="applicationId",
            zone_id="zoneId",
        )
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.assign(
            application_id="applicationId",
            zone_id="zoneId",
            owner_type="platform",
            role_id="role_id",
            role_identifier="role_identifier",
            scope_id="x",
            scope_type="x",
        )
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.roles.with_raw_response.assign(
            application_id="applicationId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleAssignment, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.roles.with_streaming_response.assign(
            application_id="applicationId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(RoleAssignment, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.assign(
                application_id="applicationId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.assign(
                application_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        )
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        role = await async_client.zones.applications.roles.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
            scope_id="x",
            scope_type="x",
        )
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.applications.roles.with_raw_response.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert role is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.applications.roles.with_streaming_response.revoke(
            role_id="roleId",
            zone_id="zoneId",
            application_id="applicationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert role is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.revoke(
                role_id="roleId",
                zone_id="",
                application_id="applicationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.revoke(
                role_id="roleId",
                zone_id="zoneId",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.zones.applications.roles.with_raw_response.revoke(
                role_id="",
                zone_id="zoneId",
                application_id="applicationId",
            )
