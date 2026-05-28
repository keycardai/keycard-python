# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InputState", "EffectiveSchema"]


class EffectiveSchema(BaseModel):
    """
    A subset of JSON Schema 2020-12 used to describe package input and output
    shapes.

    Supported keywords:
    - Structural: `type`, `properties`, `required`, `items`, `additionalProperties`
    - Annotations: `title`, `description`, `default`, `readOnly`, `writeOnly`
    - Constraints: `pattern`, `minLength`, `maxLength`, `minimum`, `maximum`,
    `minItems`, `maxItems`, `enum`, `const`, `format`

    Intentionally unsupported (reject at release time rather than silently ignore):
    - Schema combinators: `allOf`, `anyOf`, `oneOf`, `not`
    - References: `$ref`, `$dynamicRef`
    - `patternProperties`, `propertyNames`, `unevaluatedProperties`
    - Custom vocabularies and `$vocabulary`

    Dialect: JSON Schema 2020-12 (implied — authors do not include `$schema`).
    """

    additional_properties: Optional[object] = FieldInfo(alias="additionalProperties", default=None)
    """Schema for properties not named in `properties`."""

    const: Optional[object] = None
    """Constant allowed value."""

    default: Optional[object] = None
    """Default value (annotation)."""

    description: Optional[str] = None
    """Human-readable description (annotation)."""

    enum: Optional[List[object]] = None
    """Enumerated allowed values."""

    format: Optional[str] = None
    """Format hint (e.g., "uri", "uuid", "email", "date-time")."""

    items: Optional[object] = None
    """Schema for array items."""

    maximum: Optional[float] = None

    max_items: Optional[int] = FieldInfo(alias="maxItems", default=None)

    max_length: Optional[int] = FieldInfo(alias="maxLength", default=None)

    minimum: Optional[float] = None

    min_items: Optional[int] = FieldInfo(alias="minItems", default=None)

    min_length: Optional[int] = FieldInfo(alias="minLength", default=None)

    pattern: Optional[str] = None

    properties: Optional[object] = None
    """Property schemas, keyed by property name."""

    read_only: Optional[bool] = FieldInfo(alias="readOnly", default=None)
    """Read-only hint — server-populated, ignored on write."""

    required: Optional[List[str]] = None
    """Names of required properties."""

    title: Optional[str] = None
    """Human-readable title (annotation)."""

    type: Optional[Literal["object", "array", "string", "integer", "number", "boolean", "null"]] = None
    """The `type` keyword in JSON Schema 2020-12."""

    write_only: Optional[bool] = FieldInfo(alias="writeOnly", default=None)
    """Write-only hint (passwords, secrets) — never returned on read."""


class InputState(BaseModel):
    """
    Computed input state for a package — derived at response time from the
    package kind's schema and the package's input binding. Not stored.

    `effective_schema` is the full input schema (kind + binding required
    constraints merged). `effective_bindings` resolves the CEL binding to
    show actual static values and `{"$input": "path"}` references for
    install-provided fields.
    """

    effective_bindings: Optional[Dict[str, object]] = None

    effective_schema: Optional[EffectiveSchema] = None
    """
    A subset of JSON Schema 2020-12 used to describe package input and output
    shapes.

    Supported keywords:

    - Structural: `type`, `properties`, `required`, `items`, `additionalProperties`
    - Annotations: `title`, `description`, `default`, `readOnly`, `writeOnly`
    - Constraints: `pattern`, `minLength`, `maxLength`, `minimum`, `maximum`,
      `minItems`, `maxItems`, `enum`, `const`, `format`

    Intentionally unsupported (reject at release time rather than silently ignore):

    - Schema combinators: `allOf`, `anyOf`, `oneOf`, `not`
    - References: `$ref`, `$dynamicRef`
    - `patternProperties`, `propertyNames`, `unevaluatedProperties`
    - Custom vocabularies and `$vocabulary`

    Dialect: JSON Schema 2020-12 (implied — authors do not include `$schema`).
    """
