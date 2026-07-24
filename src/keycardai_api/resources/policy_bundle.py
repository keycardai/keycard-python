# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import policy_bundle_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["PolicyBundleResource", "AsyncPolicyBundleResource"]


class PolicyBundleResource(SyncAPIResource):
    """Per-user Policy Bundle resource.

    Allows clients (typically the Keycard CLI)
    to GET, PUT, and DELETE the effective Policy Set for the calling user
    on a zone. The bundle is encoded with a content-negotiated codec (currently
    only `application/vnd.keycard.policy-bundle.v1+tar+gzip`).

    ## Archive layout

    The bundle is a gzip-compressed tar archive with this logical layout:

    | Entry | Required on PUT | Notes |
    |-------|-----------------|-------|
    | `manifest.json` | **Yes** | See `PolicyBundleManifest`. The only source of the authoritative `schema.version`. |
    | `schema.cedarschema` | No | Convenience snapshot of the Cedar schema. **Ignored on PUT** — the server validates policies against its own attested schema for `manifest.schema.version`. **Always present on GET.** |
    | `policies/<public_id>.cedar` | — | One Cedar policy per file; the filename stem is the policy's public ID. |

    Decode rules: duplicate entries and unrecognized/nested entries are
    rejected (`bundle_invalid`). On PUT the manifest's `sha` fields and
    `policies[]` list are advisory — the server recomputes every digest from
    the archived bytes and derives the policy set from the `policies/` files.
    On GET every digest is authoritative.
    """

    @cached_property
    def with_raw_response(self) -> PolicyBundleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return PolicyBundleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyBundleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return PolicyBundleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        if_none_match: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Returns the effective Policy Bundle for the user identified by the zone-issued
        resource-scoped token. When no user-scope binding exists, one will be generated
        from the default set.

        The response body is a binary archive in the codec selected via the `Accept`
        header. The only codec supported today is
        `application/vnd.keycard.policy-bundle.v1+tar+gzip`. Clients SHOULD send an
        explicit `Accept` header; absent one, the server defaults to the tar+gzip codec.

        Supports conditional fetch via `If-None-Match`: when the supplied ETag matches
        the current bundle, the server responds `304 Not Modified` with no body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.keycard.policy-bundle.v1+tar+gzip", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "If-None-Match": if_none_match,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/policy/bundle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        *,
        body: FileTypes,
        if_match: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Accepts an edited Policy Bundle archive and applies it as the active user-scope
        PolicySetVersion for the calling user.

        The user's policy set is seeded from the system-default policies on first
        access, forked into customer-owned policies; a user bundle therefore contains
        only customer-owned policies. Applying an edit creates a new version of the
        affected policy, and a `new_policy` entry adds a further customer-owned policy.
        Platform-owned catalog policies are never edited in place by this operation.

        The request body codec is determined from `Content-Type`. The only codec
        supported today is `application/vnd.keycard.policy-bundle.v1+tar+gzip`.

        Supports optimistic concurrency via `If-Match`: when supplied, the server
        applies the bundle only if the supplied ETag matches the current bundle ETag;
        otherwise responds `412 Precondition Failed`.

        On success the server returns the materialized bundle (in the same codec) and
        its new `ETag`.

        Args:
          body: tar+gzip Policy Bundle archive. `manifest.json` is **required** (see
              `PolicyBundleManifest`); `schema.cedarschema` is **optional and ignored** — the
              server validates against its attested schema for `manifest.schema.version`. The
              manifest's `policies[]` list is authoritative for the resulting set: each entry
              must have a matching `policies/<public_id>.cedar` (or, for a `new_policy` entry,
              `policies/<new_policy>.cedar`) member, and a member with no manifest entry is
              dropped. Only the `sha` fields are advisory and recomputed server-side.
              Duplicate or unrecognized entries are rejected with `bundle_invalid`. See the
              **PolicyBundle** tag for the layout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.keycard.policy-bundle.v1+tar+gzip", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            "/policy/bundle",
            body=maybe_transform(body, policy_bundle_update_params.PolicyBundleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=BinaryAPIResponse,
        )

    def reset(
        self,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives the PolicySet for the calling user (if any), causing subsequent
        `GET /policy/bundle` requests to fall back to the default user policies.
        Idempotent: returns `204 No Content` even when no user-scope binding exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return self._delete(
            "/policy/bundle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=NoneType,
        )


class AsyncPolicyBundleResource(AsyncAPIResource):
    """Per-user Policy Bundle resource.

    Allows clients (typically the Keycard CLI)
    to GET, PUT, and DELETE the effective Policy Set for the calling user
    on a zone. The bundle is encoded with a content-negotiated codec (currently
    only `application/vnd.keycard.policy-bundle.v1+tar+gzip`).

    ## Archive layout

    The bundle is a gzip-compressed tar archive with this logical layout:

    | Entry | Required on PUT | Notes |
    |-------|-----------------|-------|
    | `manifest.json` | **Yes** | See `PolicyBundleManifest`. The only source of the authoritative `schema.version`. |
    | `schema.cedarschema` | No | Convenience snapshot of the Cedar schema. **Ignored on PUT** — the server validates policies against its own attested schema for `manifest.schema.version`. **Always present on GET.** |
    | `policies/<public_id>.cedar` | — | One Cedar policy per file; the filename stem is the policy's public ID. |

    Decode rules: duplicate entries and unrecognized/nested entries are
    rejected (`bundle_invalid`). On PUT the manifest's `sha` fields and
    `policies[]` list are advisory — the server recomputes every digest from
    the archived bytes and derives the policy set from the `policies/` files.
    On GET every digest is authoritative.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPolicyBundleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/keycardai/keycard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyBundleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyBundleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/keycardai/keycard-python#with_streaming_response
        """
        return AsyncPolicyBundleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        if_none_match: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Returns the effective Policy Bundle for the user identified by the zone-issued
        resource-scoped token. When no user-scope binding exists, one will be generated
        from the default set.

        The response body is a binary archive in the codec selected via the `Accept`
        header. The only codec supported today is
        `application/vnd.keycard.policy-bundle.v1+tar+gzip`. Clients SHOULD send an
        explicit `Accept` header; absent one, the server defaults to the tar+gzip codec.

        Supports conditional fetch via `If-None-Match`: when the supplied ETag matches
        the current bundle, the server responds `304 Not Modified` with no body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.keycard.policy-bundle.v1+tar+gzip", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "If-None-Match": if_none_match,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/policy/bundle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        *,
        body: FileTypes,
        if_match: str | Omit = omit,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Accepts an edited Policy Bundle archive and applies it as the active user-scope
        PolicySetVersion for the calling user.

        The user's policy set is seeded from the system-default policies on first
        access, forked into customer-owned policies; a user bundle therefore contains
        only customer-owned policies. Applying an edit creates a new version of the
        affected policy, and a `new_policy` entry adds a further customer-owned policy.
        Platform-owned catalog policies are never edited in place by this operation.

        The request body codec is determined from `Content-Type`. The only codec
        supported today is `application/vnd.keycard.policy-bundle.v1+tar+gzip`.

        Supports optimistic concurrency via `If-Match`: when supplied, the server
        applies the bundle only if the supplied ETag matches the current bundle ETag;
        otherwise responds `412 Precondition Failed`.

        On success the server returns the materialized bundle (in the same codec) and
        its new `ETag`.

        Args:
          body: tar+gzip Policy Bundle archive. `manifest.json` is **required** (see
              `PolicyBundleManifest`); `schema.cedarschema` is **optional and ignored** — the
              server validates against its attested schema for `manifest.schema.version`. The
              manifest's `policies[]` list is authoritative for the resulting set: each entry
              must have a matching `policies/<public_id>.cedar` (or, for a `new_policy` entry,
              `policies/<new_policy>.cedar`) member, and a member with no manifest entry is
              dropped. Only the `sha` fields are advisory and recomputed server-side.
              Duplicate or unrecognized entries are rejected with `bundle_invalid`. See the
              **PolicyBundle** tag for the layout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.keycard.policy-bundle.v1+tar+gzip", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": if_match,
                    "X-Client-Request-ID": x_client_request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            "/policy/bundle",
            body=await async_maybe_transform(body, policy_bundle_update_params.PolicyBundleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def reset(
        self,
        *,
        x_client_request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives the PolicySet for the calling user (if any), causing subsequent
        `GET /policy/bundle` requests to fall back to the default user policies.
        Idempotent: returns `204 No Content` even when no user-scope binding exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Client-Request-ID": x_client_request_id}), **(extra_headers or {})}
        return await self._delete(
            "/policy/bundle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=NoneType,
        )


class PolicyBundleResourceWithRawResponse:
    def __init__(self, policy_bundle: PolicyBundleResource) -> None:
        self._policy_bundle = policy_bundle

        self.retrieve = to_custom_raw_response_wrapper(
            policy_bundle.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            policy_bundle.update,
            BinaryAPIResponse,
        )
        self.reset = to_raw_response_wrapper(
            policy_bundle.reset,
        )


class AsyncPolicyBundleResourceWithRawResponse:
    def __init__(self, policy_bundle: AsyncPolicyBundleResource) -> None:
        self._policy_bundle = policy_bundle

        self.retrieve = async_to_custom_raw_response_wrapper(
            policy_bundle.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            policy_bundle.update,
            AsyncBinaryAPIResponse,
        )
        self.reset = async_to_raw_response_wrapper(
            policy_bundle.reset,
        )


class PolicyBundleResourceWithStreamingResponse:
    def __init__(self, policy_bundle: PolicyBundleResource) -> None:
        self._policy_bundle = policy_bundle

        self.retrieve = to_custom_streamed_response_wrapper(
            policy_bundle.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            policy_bundle.update,
            StreamedBinaryAPIResponse,
        )
        self.reset = to_streamed_response_wrapper(
            policy_bundle.reset,
        )


class AsyncPolicyBundleResourceWithStreamingResponse:
    def __init__(self, policy_bundle: AsyncPolicyBundleResource) -> None:
        self._policy_bundle = policy_bundle

        self.retrieve = async_to_custom_streamed_response_wrapper(
            policy_bundle.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            policy_bundle.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.reset = async_to_streamed_response_wrapper(
            policy_bundle.reset,
        )
