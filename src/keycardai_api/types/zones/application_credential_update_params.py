# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ApplicationCredentialUpdateParams",
    "IamTokenCredentialUpdate",
    "IamPasswordCredentialUpdate",
    "IamPublicKeyCredentialUpdate",
    "IamURLCredentialUpdate",
    "IamPublicCredentialUpdate",
]


class IamTokenCredentialUpdate(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    subject: Optional[str]
    """Subject identifier for the token.

    Set to null to unset, which allows any token from the provider to be accepted
    without checking application-specific claims.
    """

    type: Literal["token"]


class IamPasswordCredentialUpdate(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    type: Literal["password"]


class IamPublicKeyCredentialUpdate(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    type: Literal["public-key"]


class IamURLCredentialUpdate(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    identifier: str
    """URL of the credential (must be a valid URL)"""

    type: Literal["url"]


class IamPublicCredentialUpdate(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    identifier: str
    """Identifier for public credential, also used as OAuth 2.0 client ID"""

    type: Literal["public"]


ApplicationCredentialUpdateParams: TypeAlias = Union[
    IamTokenCredentialUpdate,
    IamPasswordCredentialUpdate,
    IamPublicKeyCredentialUpdate,
    IamURLCredentialUpdate,
    IamPublicCredentialUpdate,
]
