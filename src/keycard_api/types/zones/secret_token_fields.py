# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SecretTokenFields"]


class SecretTokenFields(BaseModel):
    token: str

    type: Literal["token"]
