# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .schema_version import SchemaVersion

__all__ = ["SchemaVersionWithZoneInfo"]


class SchemaVersionWithZoneInfo(SchemaVersion):
    is_default: bool
