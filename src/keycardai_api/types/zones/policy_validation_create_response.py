# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PolicyValidationCreateResponse",
    "Error",
    "ErrorRange",
    "ErrorRangeEnd",
    "ErrorRangeStart",
    "Warning",
    "WarningRange",
    "WarningRangeEnd",
    "WarningRangeStart",
]


class ErrorRangeEnd(BaseModel):
    """A position in the submitted policy text."""

    column: int
    """1-based column number (counts Unicode scalar values)."""

    line: int
    """1-based line number."""

    offset: int
    """0-based byte offset into the UTF-8 policy text."""


class ErrorRangeStart(BaseModel):
    """A position in the submitted policy text."""

    column: int
    """1-based column number (counts Unicode scalar values)."""

    line: int
    """1-based line number."""

    offset: int
    """0-based byte offset into the UTF-8 policy text."""


class ErrorRange(BaseModel):
    """
    Half-open source range [start, end) locating a diagnostic in the submitted policy text. Optional: present only when the engine can map the finding to a span. Populated for parse/syntax errors and for semantic findings when the policy was submitted as `cedar_raw`; absent for whole-policy semantic findings (no single span) and for policies submitted as `cedar_json` (the JSON AST carries no source locations).
    """

    end: ErrorRangeEnd
    """A position in the submitted policy text."""

    start: ErrorRangeStart
    """A position in the submitted policy text."""


class Error(BaseModel):
    message: str
    """Human-readable description of the validation issue."""

    code: Optional[str] = None
    """Machine-readable kind of the diagnostic (e.g.

    `unknown_action`, `parse_error`). Optional and additive; absent when the finding
    has no specific code.
    """

    data: Optional[Dict[str, str]] = None
    """
    Optional structured details keyed by the diagnostic `code`, so consumers need
    not parse `message`. For `unknown_action`: `{"action_uid": "..."}`.
    """

    help: Optional[str] = None
    """
    Optional advisory text, rendered by clients as secondary text below the primary
    message.
    """

    range: Optional[ErrorRange] = None
    """
    Half-open source range [start, end) locating a diagnostic in the submitted
    policy text. Optional: present only when the engine can map the finding to a
    span. Populated for parse/syntax errors and for semantic findings when the
    policy was submitted as `cedar_raw`; absent for whole-policy semantic findings
    (no single span) and for policies submitted as `cedar_json` (the JSON AST
    carries no source locations).
    """

    severity: Optional[Literal["error", "warning"]] = None
    """Severity of the diagnostic.

    Optional and additive; older clients that only read `message` can ignore it.
    Diagnostics under `errors` are `error`; those under `warnings` are `warning`.
    """


class WarningRangeEnd(BaseModel):
    """A position in the submitted policy text."""

    column: int
    """1-based column number (counts Unicode scalar values)."""

    line: int
    """1-based line number."""

    offset: int
    """0-based byte offset into the UTF-8 policy text."""


class WarningRangeStart(BaseModel):
    """A position in the submitted policy text."""

    column: int
    """1-based column number (counts Unicode scalar values)."""

    line: int
    """1-based line number."""

    offset: int
    """0-based byte offset into the UTF-8 policy text."""


class WarningRange(BaseModel):
    """
    Half-open source range [start, end) locating a diagnostic in the submitted policy text. Optional: present only when the engine can map the finding to a span. Populated for parse/syntax errors and for semantic findings when the policy was submitted as `cedar_raw`; absent for whole-policy semantic findings (no single span) and for policies submitted as `cedar_json` (the JSON AST carries no source locations).
    """

    end: WarningRangeEnd
    """A position in the submitted policy text."""

    start: WarningRangeStart
    """A position in the submitted policy text."""


class Warning(BaseModel):
    message: str
    """Human-readable description of the validation issue."""

    code: Optional[str] = None
    """Machine-readable kind of the diagnostic (e.g.

    `unknown_action`, `parse_error`). Optional and additive; absent when the finding
    has no specific code.
    """

    data: Optional[Dict[str, str]] = None
    """
    Optional structured details keyed by the diagnostic `code`, so consumers need
    not parse `message`. For `unknown_action`: `{"action_uid": "..."}`.
    """

    help: Optional[str] = None
    """
    Optional advisory text, rendered by clients as secondary text below the primary
    message.
    """

    range: Optional[WarningRange] = None
    """
    Half-open source range [start, end) locating a diagnostic in the submitted
    policy text. Optional: present only when the engine can map the finding to a
    span. Populated for parse/syntax errors and for semantic findings when the
    policy was submitted as `cedar_raw`; absent for whole-policy semantic findings
    (no single span) and for policies submitted as `cedar_json` (the JSON AST
    carries no source locations).
    """

    severity: Optional[Literal["error", "warning"]] = None
    """Severity of the diagnostic.

    Optional and additive; older clients that only read `message` can ignore it.
    Diagnostics under `errors` are `error`; those under `warnings` are `warning`.
    """


class PolicyValidationCreateResponse(BaseModel):
    errors: List[Error]
    """Validation errors. Empty array when valid."""

    schema_version: str
    """Schema version validated against (echo back)."""

    valid: bool
    """True if the policy passes schema validation with no errors."""

    warnings: List[Warning]
    """Validation warnings.

    May be non-empty even when valid is true. References to actions absent from the
    schema are reported here as per-occurrence warnings with code `unknown_action`
    (partitioned out of errors: they do not make valid false).
    """
