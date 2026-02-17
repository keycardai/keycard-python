# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import zones, invitations, organizations, service_account_token
    from .resources.invitations import InvitationsResource, AsyncInvitationsResource
    from .resources.zones.zones import ZonesResource, AsyncZonesResource
    from .resources.service_account_token import ServiceAccountTokenResource, AsyncServiceAccountTokenResource
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "KeycardAPI",
    "AsyncKeycardAPI",
    "Client",
    "AsyncClient",
]


class KeycardAPI(SyncAPIClient):
    # client options
    api_key: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous KeycardAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KEYCARD_API_API_KEY`
        - `username` from `KEYCARD_API_USERNAME`
        - `password` from `KEYCARD_API_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("KEYCARD_API_API_KEY")
        self.api_key = api_key

        if username is None:
            username = os.environ.get("KEYCARD_API_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("KEYCARD_API_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("KEYCARD_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.keycard.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def zones(self) -> ZonesResource:
        from .resources.zones import ZonesResource

        return ZonesResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def service_account_token(self) -> ServiceAccountTokenResource:
        from .resources.service_account_token import ServiceAccountTokenResource

        return ServiceAccountTokenResource(self)

    @cached_property
    def invitations(self) -> InvitationsResource:
        from .resources.invitations import InvitationsResource

        return InvitationsResource(self)

    @cached_property
    def with_raw_response(self) -> KeycardAPIWithRawResponse:
        return KeycardAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeycardAPIWithStreamedResponse:
        return KeycardAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._org_management_basic_auth, **self._vault_api_bearer_auth}

    @property
    def _org_management_basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    def _vault_api_bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either username, password or api_key to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKeycardAPI(AsyncAPIClient):
    # client options
    api_key: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKeycardAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KEYCARD_API_API_KEY`
        - `username` from `KEYCARD_API_USERNAME`
        - `password` from `KEYCARD_API_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("KEYCARD_API_API_KEY")
        self.api_key = api_key

        if username is None:
            username = os.environ.get("KEYCARD_API_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("KEYCARD_API_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("KEYCARD_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.keycard.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def zones(self) -> AsyncZonesResource:
        from .resources.zones import AsyncZonesResource

        return AsyncZonesResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def service_account_token(self) -> AsyncServiceAccountTokenResource:
        from .resources.service_account_token import AsyncServiceAccountTokenResource

        return AsyncServiceAccountTokenResource(self)

    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        from .resources.invitations import AsyncInvitationsResource

        return AsyncInvitationsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKeycardAPIWithRawResponse:
        return AsyncKeycardAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeycardAPIWithStreamedResponse:
        return AsyncKeycardAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._org_management_basic_auth, **self._vault_api_bearer_auth}

    @property
    def _org_management_basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    def _vault_api_bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either username, password or api_key to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KeycardAPIWithRawResponse:
    _client: KeycardAPI

    def __init__(self, client: KeycardAPI) -> None:
        self._client = client

    @cached_property
    def zones(self) -> zones.ZonesResourceWithRawResponse:
        from .resources.zones import ZonesResourceWithRawResponse

        return ZonesResourceWithRawResponse(self._client.zones)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def service_account_token(self) -> service_account_token.ServiceAccountTokenResourceWithRawResponse:
        from .resources.service_account_token import ServiceAccountTokenResourceWithRawResponse

        return ServiceAccountTokenResourceWithRawResponse(self._client.service_account_token)

    @cached_property
    def invitations(self) -> invitations.InvitationsResourceWithRawResponse:
        from .resources.invitations import InvitationsResourceWithRawResponse

        return InvitationsResourceWithRawResponse(self._client.invitations)


class AsyncKeycardAPIWithRawResponse:
    _client: AsyncKeycardAPI

    def __init__(self, client: AsyncKeycardAPI) -> None:
        self._client = client

    @cached_property
    def zones(self) -> zones.AsyncZonesResourceWithRawResponse:
        from .resources.zones import AsyncZonesResourceWithRawResponse

        return AsyncZonesResourceWithRawResponse(self._client.zones)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def service_account_token(self) -> service_account_token.AsyncServiceAccountTokenResourceWithRawResponse:
        from .resources.service_account_token import AsyncServiceAccountTokenResourceWithRawResponse

        return AsyncServiceAccountTokenResourceWithRawResponse(self._client.service_account_token)

    @cached_property
    def invitations(self) -> invitations.AsyncInvitationsResourceWithRawResponse:
        from .resources.invitations import AsyncInvitationsResourceWithRawResponse

        return AsyncInvitationsResourceWithRawResponse(self._client.invitations)


class KeycardAPIWithStreamedResponse:
    _client: KeycardAPI

    def __init__(self, client: KeycardAPI) -> None:
        self._client = client

    @cached_property
    def zones(self) -> zones.ZonesResourceWithStreamingResponse:
        from .resources.zones import ZonesResourceWithStreamingResponse

        return ZonesResourceWithStreamingResponse(self._client.zones)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def service_account_token(self) -> service_account_token.ServiceAccountTokenResourceWithStreamingResponse:
        from .resources.service_account_token import ServiceAccountTokenResourceWithStreamingResponse

        return ServiceAccountTokenResourceWithStreamingResponse(self._client.service_account_token)

    @cached_property
    def invitations(self) -> invitations.InvitationsResourceWithStreamingResponse:
        from .resources.invitations import InvitationsResourceWithStreamingResponse

        return InvitationsResourceWithStreamingResponse(self._client.invitations)


class AsyncKeycardAPIWithStreamedResponse:
    _client: AsyncKeycardAPI

    def __init__(self, client: AsyncKeycardAPI) -> None:
        self._client = client

    @cached_property
    def zones(self) -> zones.AsyncZonesResourceWithStreamingResponse:
        from .resources.zones import AsyncZonesResourceWithStreamingResponse

        return AsyncZonesResourceWithStreamingResponse(self._client.zones)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def service_account_token(self) -> service_account_token.AsyncServiceAccountTokenResourceWithStreamingResponse:
        from .resources.service_account_token import AsyncServiceAccountTokenResourceWithStreamingResponse

        return AsyncServiceAccountTokenResourceWithStreamingResponse(self._client.service_account_token)

    @cached_property
    def invitations(self) -> invitations.AsyncInvitationsResourceWithStreamingResponse:
        from .resources.invitations import AsyncInvitationsResourceWithStreamingResponse

        return AsyncInvitationsResourceWithStreamingResponse(self._client.invitations)


Client = KeycardAPI

AsyncClient = AsyncKeycardAPI
