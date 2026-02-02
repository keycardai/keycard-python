# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .secret_token_fields import SecretTokenFields
from .secret_password_fields import SecretPasswordFields

__all__ = ["SecretRetrieveResponse", "Data"]

Data: TypeAlias = Annotated[Union[SecretTokenFields, SecretPasswordFields], PropertyInfo(discriminator="type")]


class SecretRetrieveResponse(BaseModel):
    id: str
    """A globally unique opaque identifier"""

    created_at: datetime

    data: Data

    entity_id: str
    """A globally unique opaque identifier"""

    name: str
    """A name for the entity to be displayed in UI"""

    updated_at: datetime

    version: int

    zone_id: str
    """A globally unique opaque identifier"""

    description: Optional[str] = None
    """A description of the entity"""

    metadata: Optional[object] = None
    """A JSON object containing arbitrary metadata. Metadata will not be encrypted."""
