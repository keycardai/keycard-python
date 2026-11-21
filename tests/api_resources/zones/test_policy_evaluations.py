# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from keycardai_api import KeycardAPI, AsyncKeycardAPI
from keycardai_api.types.zones import (
    PolicyEvaluationCreateResponse,
    PolicyEvaluationListRequestsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KeycardAPI) -> None:
        policy_evaluation = client.zones.policy_evaluations.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        )
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KeycardAPI) -> None:
        policy_evaluation = client.zones.policy_evaluations.create(
            zone_id="zone_id",
            action="action",
            policy_source={
                "manifest": {
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                            "sha": "sha",
                        }
                    ],
                    "schema_version": "schema_version",
                },
                "policy": {
                    "policy_id": "policy_id",
                    "schema_version": "schema_version",
                    "version_id": "version_id",
                },
                "policy_set": {
                    "policy_set_id": "policy_set_id",
                    "version_id": "version_id",
                },
                "raw": {
                    "cedar": "cedar",
                    "schema_version": "schema_version",
                    "validate": True,
                },
            },
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
            acting_principal_id="acting_principal_id",
            authority_type="delegation",
            context={
                "claims": {
                    "acting_principal": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                    "actor": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                    "subject": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                },
                "scopes": ["string"],
                "session_id": "session_id",
            },
            subject_id="subject_id",
            subject_type="user",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KeycardAPI) -> None:
        response = client.zones.policy_evaluations.with_raw_response.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_evaluation = response.parse()
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KeycardAPI) -> None:
        with client.zones.policy_evaluations.with_streaming_response.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_evaluation = response.parse()
            assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_evaluations.with_raw_response.create(
                zone_id="",
                action="action",
                policy_source={},
                principal_id="principal_id",
                principal_type="user",
                resource_id="resource_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_requests(self, client: KeycardAPI) -> None:
        policy_evaluation = client.zones.policy_evaluations.list_requests(
            zone_id="zone_id",
        )
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_requests_with_all_params(self, client: KeycardAPI) -> None:
        policy_evaluation = client.zones.policy_evaluations.list_requests(
            zone_id="zone_id",
            after="x",
            before="x",
            expand="total_count",
            filter_active_decision=["string"],
            filter_authority_type=["string"],
            filter_has_shadow=True,
            filter_principal_id=["string"],
            filter_principal_type=["string"],
            filter_resource_id=["string"],
            filter_subject_id=["string"],
            filter_subject_type=["string"],
            limit=1,
            order="asc",
            query_action=["x"],
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_requests(self, client: KeycardAPI) -> None:
        response = client.zones.policy_evaluations.with_raw_response.list_requests(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_evaluation = response.parse()
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_requests(self, client: KeycardAPI) -> None:
        with client.zones.policy_evaluations.with_streaming_response.list_requests(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_evaluation = response.parse()
            assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_requests(self, client: KeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.policy_evaluations.with_raw_response.list_requests(
                zone_id="",
            )


class TestAsyncPolicyEvaluations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeycardAPI) -> None:
        policy_evaluation = await async_client.zones.policy_evaluations.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        )
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_evaluation = await async_client.zones.policy_evaluations.create(
            zone_id="zone_id",
            action="action",
            policy_source={
                "manifest": {
                    "entries": [
                        {
                            "policy_id": "policy_id",
                            "policy_version_id": "policy_version_id",
                            "sha": "sha",
                        }
                    ],
                    "schema_version": "schema_version",
                },
                "policy": {
                    "policy_id": "policy_id",
                    "schema_version": "schema_version",
                    "version_id": "version_id",
                },
                "policy_set": {
                    "policy_set_id": "policy_set_id",
                    "version_id": "version_id",
                },
                "raw": {
                    "cedar": "cedar",
                    "schema_version": "schema_version",
                    "validate": True,
                },
            },
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
            acting_principal_id="acting_principal_id",
            authority_type="delegation",
            context={
                "claims": {
                    "acting_principal": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                    "actor": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                    "subject": {
                        "email": "email",
                        "groups": ["string"],
                        "issuer_claims": {"foo": "bar"},
                    },
                },
                "scopes": ["string"],
                "session_id": "session_id",
            },
            subject_id="subject_id",
            subject_type="user",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_evaluations.with_raw_response.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_evaluation = await response.parse()
        assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_evaluations.with_streaming_response.create(
            zone_id="zone_id",
            action="action",
            policy_source={},
            principal_id="principal_id",
            principal_type="user",
            resource_id="resource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_evaluation = await response.parse()
            assert_matches_type(PolicyEvaluationCreateResponse, policy_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_evaluations.with_raw_response.create(
                zone_id="",
                action="action",
                policy_source={},
                principal_id="principal_id",
                principal_type="user",
                resource_id="resource_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_requests(self, async_client: AsyncKeycardAPI) -> None:
        policy_evaluation = await async_client.zones.policy_evaluations.list_requests(
            zone_id="zone_id",
        )
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_requests_with_all_params(self, async_client: AsyncKeycardAPI) -> None:
        policy_evaluation = await async_client.zones.policy_evaluations.list_requests(
            zone_id="zone_id",
            after="x",
            before="x",
            expand="total_count",
            filter_active_decision=["string"],
            filter_authority_type=["string"],
            filter_has_shadow=True,
            filter_principal_id=["string"],
            filter_principal_type=["string"],
            filter_resource_id=["string"],
            filter_subject_id=["string"],
            filter_subject_type=["string"],
            limit=1,
            order="asc",
            query_action=["x"],
            sort="created_at",
            x_api_version="X-API-Version",
            x_client_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_requests(self, async_client: AsyncKeycardAPI) -> None:
        response = await async_client.zones.policy_evaluations.with_raw_response.list_requests(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_evaluation = await response.parse()
        assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_requests(self, async_client: AsyncKeycardAPI) -> None:
        async with async_client.zones.policy_evaluations.with_streaming_response.list_requests(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_evaluation = await response.parse()
            assert_matches_type(PolicyEvaluationListRequestsResponse, policy_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_requests(self, async_client: AsyncKeycardAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.policy_evaluations.with_raw_response.list_requests(
                zone_id="",
            )
