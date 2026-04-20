# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SchemaVersion"]


class SchemaVersion(BaseModel):
    """
    A versioned Cedar schema that defines the entity model, actions, and
    context shape used for policy evaluation. The schema contains the valid
    entity types (User, Application, Resource), their attributes, and the
    allowed attribute values. See the Credentials API spec for a full
    reference of entity attributes and valid values.
    """

    created_at: datetime

    status: Literal["active", "deprecated", "archived"]
    """Controls what can be done with this schema version:

    - `"active"` - new policy versions can be created and validated against it.
    - `"deprecated"` - superseded by a newer version but still accepts new policy
      versions.
    - `"archived"` - closed to new policy versions. Existing policy set versions
      pinned to this schema still evaluate normally.
    """

    updated_at: datetime

    version: str

    archived_at: Optional[datetime] = None

    cedar_schema: Optional[str] = None
    """Cedar schema in human-readable syntax. Populated when format=cedar."""

    cedar_schema_json: Optional[object] = None
    """Cedar schema as JSON object. Populated when format=json (default)."""

    deprecated_at: Optional[datetime] = None
