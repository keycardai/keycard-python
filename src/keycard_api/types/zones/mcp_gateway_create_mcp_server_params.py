# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["McpGatewayCreateMcpServerParams", "Downstream", "Upstream", "UpstreamProvider"]


class McpGatewayCreateMcpServerParams(TypedDict, total=False):
    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    downstream: Required[Downstream]
    """Downstream MCP server config"""

    upstream: Required[Upstream]
    """Upstream MCP server config"""

    upstream_provider: Required[UpstreamProvider]
    """Credential provider for the upstream connection"""


class Downstream(TypedDict, total=False):
    """Downstream MCP server config"""

    slug: str
    """URL-safe identifier, unique within the zone"""


class Upstream(TypedDict, total=False):
    """Upstream MCP server config"""

    identifier: Required[str]
    """User specified identifier, unique within the zone"""

    name: Required[str]
    """Human-readable name"""


class UpstreamProvider(TypedDict, total=False):
    """Credential provider for the upstream connection"""

    identifier: Required[str]
    """User specified identifier, unique within the zone"""

    name: Required[str]
    """Human-readable name"""
