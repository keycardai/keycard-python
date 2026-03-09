# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EncryptionKeyAwsKmsConfig"]


class EncryptionKeyAwsKmsConfig(BaseModel):
    """AWS KMS configuration for zone encryption.

    When not specified, the default Keycard Cloud encryption key will be used.
    """

    arn: str
    """AWS KMS Key ARN for encrypting the zone's data"""

    type: Literal["aws"]
