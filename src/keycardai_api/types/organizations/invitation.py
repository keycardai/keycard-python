# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .invitation_status import InvitationStatus
from .organization_role import OrganizationRole

__all__ = ["Invitation"]


class Invitation(BaseModel):
    id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    created_at: datetime
    """The time the entity was created in utc"""

    created_by: str
    """ID of the user who created the invitation"""

    email: str
    """Email address for the invitation"""

    expires_at: datetime
    """When the invitation expires"""

    organization_id: str
    """Identifier for API resources. A 26-char nanoid (URL/DNS safe)."""

    role: OrganizationRole
    """Role that will be assigned when invitation is accepted"""

    status: InvitationStatus
    """Status of an invitation"""

    updated_at: datetime
    """The time the entity was mostly recently updated in utc"""

    bounce_type: Optional[Literal["permanent", "transient", "undetermined"]] = None
    """Kind of bounce when `delivery_outcome` is `bounced`.

    `permanent` means the address does not accept mail; the provider suppresses
    later sends to it until it is removed from the suppression list. `transient`
    means a temporary rejection, such as a full mailbox. `undetermined` means the
    provider could not tell.
    """

    delivery_outcome: Optional[Literal["delayed", "delivered", "failed", "suppressed", "bounced", "complained"]] = None
    """
    What happened to the most recent invitation email after the provider accepted it
    (`delivery_status` is `sent`). `delayed` means the recipient's server has not
    accepted it yet. `delivered` means the recipient's server accepted it. `failed`
    means the provider could not send it. `suppressed` means the provider did not
    send it because the address bounced or complained before. `bounced` means the
    recipient's server rejected it; see `bounce_type`. `complained` means the
    recipient marked it as spam. Absent until an outcome is known, and for
    invitations sent before outcomes were tracked. Cleared on resend. `delivered`
    can later change to `complained` within the 24 hours the outcome is tracked.
    """

    delivery_state_age_seconds: Optional[int] = None
    """
    Whole seconds in the current user-visible delivery state, calculated by the
    server. Omitted when the state or its timestamp is unknown.
    """

    delivery_status: Optional[Literal["queued", "sending", "sent", "failed", "expired"]] = None
    """Delivery state of the most recent invitation email.

    `queued` and `sending` mean the email service still holds the message. `sent`
    means the provider accepted it. `failed` means the email service could not be
    reached or rejected the message. `expired` means the invitation expired before
    the message was delivered. Absent for invitations created before delivery
    tracking existed.
    """

    delivery_updated_at: Optional[datetime] = None
    """When `delivery_outcome` last changed in the email service."""

    permissions: Optional[Dict[str, Dict[str, bool]]] = None
    """
    Permissions granted to the authenticated principal for this resource. Only
    populated when the 'expand[]=permissions' query parameter is provided. Keys are
    resource types (e.g., "organizations"), values are objects mapping permission
    names to boolean values indicating if the permission is granted.
    """

    resend_available: Optional[bool] = None
    """Whether this invitation can reserve a resend at response time.

    Does not account for organization policy, rate limits, or concurrent changes.
    """
