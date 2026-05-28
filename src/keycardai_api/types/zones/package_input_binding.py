# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PackageInputBinding", "Schema"]


class Schema(BaseModel):
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


class PackageInputBinding(BaseModel):
    """Input binding for a package.

    `schema` constrains install-level inputs. `bindings` is a CEL expression
    that assembles the flat input map — static values are CEL literals,
    install-provided values are `pkg.inputs.X` references. Evaluated at
    provisioning time to produce the `entities.inputs` map for entity bindings.
    """

    bindings: Optional[str] = None
    """
    CEL expression assembling the flat input map from static values and
    install-provided values (referenced via `pkg.inputs.X`).

    Scope:

    - `pkg.inputs` — install-supplied values conforming to `schema`.
    """

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
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
