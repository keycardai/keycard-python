# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .url import URL
from .token import Token
from .public import Public
from .password import Password
from .public_key import PublicKey

__all__ = ["Credential"]

Credential: TypeAlias = Union[Token, Password, PublicKey, URL, Public]
