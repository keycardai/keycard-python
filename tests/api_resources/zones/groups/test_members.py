# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones.groups import GroupMember, MemberListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        member = client.zones.groups.members.list(
            group_id="groupId",
            zone_id="zoneId",
        )
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        member = client.zones.groups.members.list(
            group_id="groupId",
            zone_id="zoneId",
            after="x",
            before="x",
            expand="total_count",
            filter_id="string",
            limit=1,
            query="x",
        )
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.groups.members.with_raw_response.list(
            group_id="groupId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.groups.members.with_streaming_response.list(
            group_id="groupId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.groups.members.with_raw_response.list(
                group_id="groupId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zones.groups.members.with_raw_response.list(
                group_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: KeycardAPI) -> None:
        member = client.zones.groups.members.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: KeycardAPI) -> None:
        response = client.zones.groups.members.with_raw_response.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: KeycardAPI) -> None:
        with client.zones.groups.members.with_streaming_response.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.groups.members.with_raw_response.add(
                group_id="groupId",
                zone_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zones.groups.members.with_raw_response.add(
                group_id="",
                zone_id="zoneId",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: KeycardAPI) -> None:
        member = client.zones.groups.members.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        )
        assert member is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: KeycardAPI) -> None:
        response = client.zones.groups.members.with_raw_response.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: KeycardAPI) -> None:
        with client.zones.groups.members.with_streaming_response.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.groups.members.with_raw_response.remove(
                user_id="userId",
                zone_id="",
                group_id="groupId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.zones.groups.members.with_raw_response.remove(
                user_id="userId",
                zone_id="zoneId",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zones.groups.members.with_raw_response.remove(
                user_id="",
                zone_id="zoneId",
                group_id="groupId",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        member = await async_client.zones.groups.members.list(
            group_id="groupId",
            zone_id="zoneId",
        )
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        member = await async_client.zones.groups.members.list(
            group_id="groupId",
            zone_id="zoneId",
            after="x",
            before="x",
            expand="total_count",
            filter_id="string",
            limit=1,
            query="x",
        )
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.groups.members.with_raw_response.list(
            group_id="groupId",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.groups.members.with_streaming_response.list(
            group_id="groupId",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.list(
                group_id="groupId",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.list(
                group_id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncKeycardAPI) -> None:
        member = await async_client.zones.groups.members.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        )
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.groups.members.with_raw_response.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(GroupMember, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.groups.members.with_streaming_response.add(
            group_id="groupId",
            zone_id="zoneId",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(GroupMember, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.add(
                group_id="groupId",
                zone_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.add(
                group_id="",
                zone_id="zoneId",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncKeycardAPI) -> None:
        member = await async_client.zones.groups.members.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        )
        assert member is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.groups.members.with_raw_response.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.groups.members.with_streaming_response.remove(
            user_id="userId",
            zone_id="zoneId",
            group_id="groupId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.remove(
                user_id="userId",
                zone_id="",
                group_id="groupId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.remove(
                user_id="userId",
                zone_id="zoneId",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zones.groups.members.with_raw_response.remove(
                user_id="",
                zone_id="zoneId",
                group_id="groupId",
            )
