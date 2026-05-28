# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .input_state import InputState
from .package_draft import PackageDraft
from .package_source import PackageSource
from .package_input_binding import PackageInputBinding
from .package_output_binding import PackageOutputBinding
from .packages.package_version import PackageVersion

__all__ = ["Package", "Link"]


class Link(BaseModel):
    """
    A directed, typed relationship from one entity (the subject) to another
    (the target).

    Follows the structure of RFC 7033 JRD link objects, adapted for intra-graph
    entity references. The subject is the entity whose `links` array contains
    this link.
    """

    href: str
    """Target reference.

    Fragment URIs (`#name`) reference other entities in the same graph by their
    local name (the key in the entity map). Absolute paths and URLs reference
    external resources outside the graph.
    """

    rel: str
    """Link relation type."""

    properties: Optional[Dict[str, object]] = None
    """Additional metadata keyed by property name."""

    titles: Optional[Dict[str, str]] = None
    """Human-readable titles keyed by BCP 47 language tag."""

    type: Optional[str] = None
    """
    Media type of the target resource (per RFC 7033 section 4.4.4.3). Applies to
    external `href`s; typically omitted for intra-graph references.
    """


class Package(BaseModel):
    id: str

    created_at: datetime

    kind: str

    name: str

    slug: str
    """Server-populated URL-friendly identifier."""

    updated_at: datetime

    current_version: Optional[PackageVersion] = None

    description: Optional[str] = None

    draft: Optional[PackageDraft] = None

    icon_url: Optional[str] = None

    input_state: Optional[InputState] = None
    """
    Computed input state for a package — derived at response time from the package
    kind's schema and the package's input binding. Not stored.

    `effective_schema` is the full input schema (kind + binding required constraints
    merged). `effective_bindings` resolves the CEL binding to show actual static
    values and `{"$input": "path"}` references for install-provided fields.
    """

    inputs: Optional[PackageInputBinding] = None
    """Input binding for a package.

    `schema` constrains install-level inputs. `bindings` is a CEL expression that
    assembles the flat input map — static values are CEL literals, install-provided
    values are `pkg.inputs.X` references. Evaluated at provisioning time to produce
    the `entities.inputs` map for entity bindings.
    """

    links: Optional[List[Link]] = None

    outputs: Optional[PackageOutputBinding] = None
    """Output binding for a package.

    `schema` describes the flat outputs surfaced on an install. `bindings` is a CEL
    expression — a map literal whose keys match `schema.properties` and whose values
    project fields out of the resolved entity graph. Evaluated after the provisioner
    has resolved all entities.
    """

    properties: Optional[Dict[str, object]] = None
    """Vocabulary-defined metadata properties, keyed by property URN.

    Known properties are declared with their schemas; additional properties with
    custom URNs are permitted via `Record<unknown>`.

    Each property carries `x-subject-types` indicating which entity types it applies
    to. Properties with `draft/` in the URN are experimental and carry
    `x-internal: true`.
    """

    source: Optional[PackageSource] = None
    """Provenance info for a package originating from an ancestor catalog."""

    tags: Optional[List[str]] = None
