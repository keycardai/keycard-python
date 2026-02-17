# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keycard_api import KeycardAPI, AsyncKeycardAPI
from tests.utils import assert_matches_type
from keycard_api.types.zones import (
    Credential,
    ApplicationCredentialListResponse,
    ApplicationCredentialCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplicationCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
            subject="subject",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                provider_id="provider_id",
                type="token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                type="password",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_3(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                jwks_uri="https://example.com",
                type="public-key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_4(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                identifier="https://example.com",
                type="url",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_5(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                type="public",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            subject="subject",
            type="token",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            type="password",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            type="public-key",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            identifier="https://example.com",
            type="url",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            identifier="identifier",
            type="public",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_5(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.list(
            zone_id="zoneId",
        )
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.list(
            zone_id="zoneId",
            after="x",
            application_id="applicationId",
            before="x",
            cursor="cursor",
            expand="total_count",
            limit=1,
            slug="slug",
        )
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: KeycardAPI) -> None:
        application_credential = client.zones.application_credentials.delete(
            id="id",
            zone_id="zoneId",
        )
        assert application_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KeycardAPI) -> None:
        response = client.zones.application_credentials.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = response.parse()
        assert application_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KeycardAPI) -> None:
        with client.zones.application_credentials.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = response.parse()
            assert application_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.application_credentials.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zones.application_credentials.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )


class TestAsyncApplicationCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
            subject="subject",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            provider_id="provider_id",
            type="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                provider_id="provider_id",
                type="token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                type="password",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            jwks_uri="https://example.com",
            type="public-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                jwks_uri="https://example.com",
                type="public-key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            identifier="https://example.com",
            type="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                identifier="https://example.com",
                type="url",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
            identifier="identifier",
        )
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.create(
            zone_id="zoneId",
            application_id="application_id",
            type="public",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialCreateResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.create(
                zone_id="",
                application_id="application_id",
                type="public",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.retrieve(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.retrieve(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.retrieve(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.retrieve(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.retrieve(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            subject="subject",
            type="token",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            type="password",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            type="public-key",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            identifier="https://example.com",
            type="url",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.update(
            id="id",
            zone_id="zoneId",
            identifier="identifier",
            type="public",
        )
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.update(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(Credential, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.update(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(Credential, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.update(
                id="",
                zone_id="zoneId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.list(
            zone_id="zoneId",
        )
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.list(
            zone_id="zoneId",
            after="x",
            application_id="applicationId",
            before="x",
            cursor="cursor",
            expand="total_count",
            limit=1,
            slug="slug",
        )
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.list(
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.list(
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert_matches_type(ApplicationCredentialListResponse, application_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKeycardAPI) -> None:
        application_credential = await async_client.zones.application_credentials.delete(
            id="id",
            zone_id="zoneId",
        )
        assert application_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.application_credentials.with_raw_response.delete(
            id="id",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application_credential = await response.parse()
        assert application_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.application_credentials.with_streaming_response.delete(
            id="id",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application_credential = await response.parse()
            assert application_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.delete(
                id="id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zones.application_credentials.with_raw_response.delete(
                id="",
                zone_id="zoneId",
            )
