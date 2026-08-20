from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

SCHEMA_VERSION = "1.0"
APP_VERSION = "1.0.0"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class BBox(BaseModel):
    """Normalized PDF-page bounding box in top-left origin coordinates."""

    x0: float
    y0: float
    x1: float
    y1: float

    @model_validator(mode="after")
    def validate_box(self) -> "BBox":
        vals = (self.x0, self.y0, self.x1, self.y1)
        if any(v < 0.0 or v > 1.0 for v in vals):
            raise ValueError("bbox coordinates must be normalized to [0, 1]")
        if self.x1 <= self.x0 or self.y1 <= self.y0:
            raise ValueError("bbox must have positive width and height")
        return self


class PageInfo(BaseModel):
    page_index: int = Field(ge=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


class DocumentInfo(BaseModel):
    document_id: str
    filename: str
    pdf_sha256: str
    page_count: int = Field(ge=1)
    pages: list[PageInfo]

    @model_validator(mode="after")
    def pages_match(self) -> "DocumentInfo":
        if len(self.pages) != self.page_count:
            raise ValueError("page_count must equal number of pages")
        indices = [p.page_index for p in self.pages]
        if indices != list(range(self.page_count)):
            raise ValueError("pages must be zero-indexed and contiguous")
        return self


class PipelineInfo(BaseModel):
    name: str = "unknown"
    version: str | None = None
    ocr_engine: str | None = None
    ocr_version: str | None = None
    config_hash: str | None = None
    processed_at: str | None = None
    adapter: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Region(BaseModel):
    region_id: str
    source_region_id: str | None = None
    page: int = Field(ge=0)
    bbox: BBox
    type: str
    text: str = ""
    ocr_confidence: float | None = Field(default=None, ge=0.0, le=1.0)
    reading_order: int | None = None
    heading_level: int | None = Field(default=None, ge=1, le=6)
    heading_level_source: str | None = None
    heading_level_uncertain: bool = False
    uncertainty_reason: str | None = None
    origin: Literal["machine", "human"] = "machine"
    ignored: bool = False
    uncertain: bool = False
    note: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class AnnotationState(BaseModel):
    schema_version: str = SCHEMA_VERSION
    document: DocumentInfo
    pipeline: PipelineInfo = Field(default_factory=PipelineInfo)
    regions: list[Region]
    state_revision: int = 0
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_regions(self) -> "AnnotationState":
        ids = [r.region_id for r in self.regions]
        if len(ids) != len(set(ids)):
            raise ValueError("region_id values must be unique")
        for region in self.regions:
            if region.page >= self.document.page_count:
                raise ValueError(f"region {region.region_id} references invalid page {region.page}")
        return self


class StatePatch(BaseModel):
    regions: list[Region] = Field(default_factory=list)


class AnnotationEvent(BaseModel):
    event_id: str
    session_id: str
    sequence: int = Field(ge=1)
    timestamp_utc: str
    annotator_id: str
    action: str
    mutates_state: bool = False
    target_region_ids: list[str] = Field(default_factory=list)
    page: int | None = None
    before: StatePatch | None = None
    after: StatePatch | None = None
    target_event_id: str | None = None
    reason_code: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class SessionMeta(BaseModel):
    schema_version: str = SCHEMA_VERSION
    app_version: str = APP_VERSION
    session_id: str
    document_id: str
    filename: str
    annotator_id: str
    created_at: str
    updated_at: str
    finalised_at: str | None = None
    status: Literal["active", "approved"] = "active"
    active_seconds: int = 0
    initial_state_sha256: str | None = None
    events_sha256: str | None = None
    final_state_sha256: str | None = None
    replay_valid: bool | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class CommandRequest(BaseModel):
    action: str
    region_id: str | None = None
    region_ids: list[str] = Field(default_factory=list)
    payload: dict[str, Any] = Field(default_factory=dict)
    reason_code: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class InteractionRequest(BaseModel):
    action: str
    page: int | None = None
    region_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)




class ReviewChecklist(BaseModel):
    """Minimal sign-off checklist used to make "satisfactory" consistent across reviewers."""

    checklist_version: str = "1.0"
    reviewed_all_pages: bool = False
    missing_spurious_regions_checked: bool = False
    boundaries_checked: bool = False
    types_checked: bool = False
    structure_checked: bool = False
    uncertainty_documented: bool = False

    @model_validator(mode="after")
    def require_all_checks(self) -> "ReviewChecklist":
        checks = [
            self.reviewed_all_pages,
            self.missing_spurious_regions_checked,
            self.boundaries_checked,
            self.types_checked,
            self.structure_checked,
            self.uncertainty_documented,
        ]
        if not all(checks):
            raise ValueError("All review checklist items must be confirmed before finalisation")
        return self


class FinaliseRequest(BaseModel):
    checklist: ReviewChecklist
    approval_note: str | None = Field(default=None, max_length=2000)


class ActivityRequest(BaseModel):
    seconds: int = Field(ge=1, le=60)
