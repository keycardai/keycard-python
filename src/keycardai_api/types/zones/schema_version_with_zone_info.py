# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .schema_version import SchemaVersion

__all__ = ["SchemaVersionWithZoneInfo"]


class SchemaVersionWithZoneInfo(SchemaVersion):
    """
    A versioned Cedar schema that defines the entity model, actions, and
    context shape used for policy evaluation. The schema contains the valid
    entity types (User, Application, Resource), their attributes, and the
    allowed attribute values. See the Credentials API spec for a full
    reference of entity attributes and valid values.
    """

    is_default: bool
    """Whether this is the zone's default schema.

    Clients use this to pre-select which schema to write policies against. Has no
    effect on evaluation.
    """
