# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .package_input_binding import PackageInputBinding
from .package_output_binding import PackageOutputBinding

__all__ = ["PackageDraft", "Link"]


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


class PackageDraft(BaseModel):
    id: str

    manifest_sha: str

    name: str

    updated_at: datetime

    description: Optional[str] = None

    icon_url: Optional[str] = None

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

    tags: Optional[List[str]] = None
