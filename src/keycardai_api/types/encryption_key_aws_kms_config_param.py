# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EncryptionKeyAwsKmsConfigParam"]


class EncryptionKeyAwsKmsConfigParam(TypedDict, total=False):
    """AWS KMS configuration for zone encryption.

    When not specified, the default Keycard Cloud encryption key will be used.
    """

    arn: Required[str]
    """AWS KMS Key ARN for encrypting the zone's data"""

    type: Required[Literal["aws"]]
