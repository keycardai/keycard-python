# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .secret_token_fields_param import SecretTokenFieldsParam
from .secret_password_fields_param import SecretPasswordFieldsParam

__all__ = ["SecretUpdateParams", "Data"]


class SecretUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """A globally unique opaque identifier"""

    data: Data

    description: str
    """A description of the entity"""

    metadata: object
    """A JSON object containing arbitrary metadata. Metadata will not be encrypted."""

    name: str
    """A name for the entity to be displayed in UI"""

    x_client_request_id: Annotated[str, PropertyInfo(alias="X-Client-Request-ID")]


Data: TypeAlias = Union[SecretTokenFieldsParam, SecretPasswordFieldsParam]
