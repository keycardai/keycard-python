# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.organizations.service_accounts import (
    CredentialListResponse,
    CredentialCreateResponse,
    ServiceAccountCredential,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
            description="description",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.organizations.service_accounts.credentials.with_raw_response.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.organizations.service_accounts.credentials.with_streaming_response.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.create(
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.create(
                service_account_id="",
                organization_id="x",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            expand=["permissions"],
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.organizations.service_accounts.credentials.with_raw_response.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.organizations.service_accounts.credentials.with_streaming_response.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(ServiceAccountCredential, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            description="description",
            name="name",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KeycardAPI) -> None:
        response = client.organizations.service_accounts.credentials.with_raw_response.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KeycardAPI) -> None:
        with client.organizations.service_accounts.credentials.with_streaming_response.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(ServiceAccountCredential, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            after="x",
            before="x",
            expand=["permissions"],
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.organizations.service_accounts.credentials.with_raw_response.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.organizations.service_accounts.credentials.with_streaming_response.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.list(
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.list(
                service_account_id="",
                organization_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: KeycardAPI) -> None:
        credential = client.organizations.service_accounts.credentials.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.organizations.service_accounts.credentials.with_raw_response.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.organizations.service_accounts.credentials.with_streaming_response.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
            description="description",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.service_accounts.credentials.with_raw_response.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.service_accounts.credentials.with_streaming_response.create(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.create(
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.create(
                service_account_id="",
                organization_id="x",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            expand=["permissions"],
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.service_accounts.credentials.with_raw_response.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.service_accounts.credentials.with_streaming_response.retrieve(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(ServiceAccountCredential, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.retrieve(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            description="description",
            name="name",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.service_accounts.credentials.with_raw_response.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(ServiceAccountCredential, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.service_accounts.credentials.with_streaming_response.update(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(ServiceAccountCredential, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.update(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            after="x",
            before="x",
            expand=["permissions"],
            limit=1,
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.service_accounts.credentials.with_raw_response.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.service_accounts.credentials.with_streaming_response.list(
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.list(
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.list(
                service_account_id="",
                organization_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        credential = await async_client.organizations.service_accounts.credentials.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.organizations.service_accounts.credentials.with_raw_response.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert credential is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.organizations.service_accounts.credentials.with_streaming_response.delete(
            credential_id="ab3def8hij2klm9opq5rst7uvw",
            organization_id="x",
            service_account_id="ab3def8hij2klm9opq5rst7uvw",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="ab3def8hij2klm9opq5rst7uvw",
                organization_id="x",
                service_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.organizations.service_accounts.credentials.with_raw_response.delete(
                credential_id="",
                organization_id="x",
                service_account_id="ab3def8hij2klm9opq5rst7uvw",
            )
