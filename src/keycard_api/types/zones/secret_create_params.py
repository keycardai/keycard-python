# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretCreateParams", "Data", "DataVaultAPISecretTokenFields", "DataVaultAPISecretPasswordFields"]


class SecretCreateParams(TypedDict, total=False):
    data: Required[Data]

    entity_id: Required[str]
    """A globally unique opaque identifier"""

    name: Required[str]
    """A name for the entity to be displayed in UI"""

    description: str
    """A description of the entity"""

    metadata: object
    """A JSON object containing arbitrary metadata. Metadata will not be encrypted."""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


class DataVaultAPISecretTokenFields(TypedDict, total=False):
    token: Required[str]

    type: Required[Literal["token"]]


class DataVaultAPISecretPasswordFields(TypedDict, total=False):
    password: Required[str]

    type: Required[Literal["password"]]

    username: Required[str]


Data: TypeAlias = Union[DataVaultAPISecretTokenFields, DataVaultAPISecretPasswordFields]
