# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .install_status import InstallStatus

__all__ = ["Install", "Link"]


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


class Install(BaseModel):
    id: str

    created_at: datetime

    package_id: str

    package_slug: str

    status: InstallStatus

    updated_at: datetime

    inputs: Optional[Dict[str, object]] = None
    """
    Install-specific input values that supplement the package's inputs. Merged with
    the package's input values to form the complete `entities.inputs` for entity
    binding evaluation.
    """

    links: Optional[List[Link]] = None

    org_id: Optional[str] = None

    outputs: Optional[Dict[str, object]] = None
    """
    Resolved output values produced by the provisioner, conforming to the package's
    `Package.outputs.schema`. Flat — the provisioner evaluates
    `Package.outputs.bindings` against the resolved entity graph.
    """

    package_version: Optional[int] = None

    zone_id: Optional[str] = None
