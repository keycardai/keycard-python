# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .provider import Provider
from ..._models import BaseModel
from .applications.resource import Resource

__all__ = ["McpGatewayCreateServerResponse"]


class McpGatewayCreateServerResponse(BaseModel):
    """
    Response containing the created upstream provider, upstream resource, and downstream resource for an MCP server
    """

    downstream_resource: Resource
    """A Resource is a system that exposes protected information or functionality.

    It requires authentication of the requesting actor, which may be a user or
    application, before allowing access.
    """

    upstream_provider: Provider
    """
    A Provider is a system that supplies access to Resources and allows actors
    (Users or Applications) to authenticate.
    """

    upstream_resource: Resource
    """A Resource is a system that exposes protected information or functionality.

    It requires authentication of the requesting actor, which may be a user or
    application, before allowing access.
    """
