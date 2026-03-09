# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretPasswordFieldsParam"]


class SecretPasswordFieldsParam(TypedDict, total=False):
    password: Required[str]

    type: Required[Literal["password"]]

    username: Required[str]
