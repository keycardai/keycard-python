# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types import InvitationAcceptResponse, InvitationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        invitation = client.invitations.retrieve(
            token="token",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        invitation = client.invitations.retrieve(
            token="token",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.invitations.with_raw_response.retrieve(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.invitations.with_streaming_response.retrieve(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.invitations.with_raw_response.retrieve(
                token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept(self, client: KeycardAPI) -> None:
        invitation = client.invitations.accept(
            token="token",
        )
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept_with_all_params(self, client: KeycardAPI) -> None:
        invitation = client.invitations.accept(
            token="token",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_accept(self, client: KeycardAPI) -> None:
        response = client.invitations.with_raw_response.accept(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_accept(self, client: KeycardAPI) -> None:
        with client.invitations.with_streaming_response.accept(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_accept(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.invitations.with_raw_response.accept(
                token="",
            )


class TestAsyncInvitations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        invitation = await async_client.invitations.retrieve(
            token="token",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        invitation = await async_client.invitations.retrieve(
            token="token",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.invitations.with_raw_response.retrieve(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.invitations.with_streaming_response.retrieve(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.invitations.with_raw_response.retrieve(
                token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept(self, async_client: AsyncKeycardAPI) -> None:
        invitation = await async_client.invitations.accept(
            token="token",
        )
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        invitation = await async_client.invitations.accept(
            token="token",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_accept(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.invitations.with_raw_response.accept(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_accept(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.invitations.with_streaming_response.accept(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationAcceptResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_accept(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.invitations.with_raw_response.accept(
                token="",
            )
