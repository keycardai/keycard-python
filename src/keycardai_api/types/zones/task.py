# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .task_status import TaskStatus
from .task_operation import TaskOperation

__all__ = ["Task", "Link", "Warning", "WarningDetail"]


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


class WarningDetail(BaseModel):
    code: Literal[
        "validation_error",
        "bad_request",
        "unauthorized",
        "forbidden",
        "not_found",
        "conflict",
        "rate_limit_exceeded",
        "internal_error",
        "service_unavailable",
    ]

    field: str
    """valid json path for request body"""

    message: str
    """error message for specific error"""


class Warning(BaseModel):
    """Represents an error that has occurred in the Keycard system."""

    code: Literal[
        "validation_error",
        "bad_request",
        "unauthorized",
        "forbidden",
        "not_found",
        "conflict",
        "rate_limit_exceeded",
        "internal_error",
        "service_unavailable",
    ]

    details: List[WarningDetail]

    message: str
    """summary of the error"""

    path: str

    request_id: str

    status: int
    """HTTP Status Code"""

    timestamp: datetime


class Task(BaseModel):
    id: str

    created_at: datetime

    operation: TaskOperation

    status: TaskStatus

    updated_at: datetime

    error_message: Optional[str] = None

    install_id: Optional[str] = None

    links: Optional[List[Link]] = None

    package_id: Optional[str] = None

    package_slug: Optional[str] = None

    package_version: Optional[int] = None

    warnings: Optional[List[Warning]] = None
    """Informational warnings about the task outcome.

    For delete tasks, warns when adopted entities (pre-existing resources not
    created by the catalog) will be preserved rather than deleted.
    """
