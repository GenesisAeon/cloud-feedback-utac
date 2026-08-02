"""Structured, honestly-labeled collection of real equilibrium-climate-
sensitivity (ECS) estimates driven by cloud feedback research.

No UTAC/CREP/AFET framing -- see constants.py and DISCLAIMER.md.
"""

from __future__ import annotations

from dataclasses import dataclass

from cloud_feedback_utac.constants import (
    AR6_ECS_BEST_ESTIMATE_C,
    AR6_ECS_LIKELY_RANGE_C,
    MYERS_2021_CITATION,
    TAN_2025_CITATION,
    TAN_2025_ECS_C,
    TAN_2025_ECS_UNCERTAINTY_1SIGMA_C,
)


@dataclass(frozen=True)
class ECSEstimate:
    label: str
    ecs_c: float | None
    """Point estimate in degrees C, or None if only a qualitative
    direction ("moderate"/"higher") is reported."""
    range_c: tuple[float, float] | None
    citation: str
    leans: str
    """One of "moderate", "higher" -- an honest label for which direction
    this estimate points relative to the AR6 best estimate, not a claim
    that either is settled."""


ALL_ECS_ESTIMATES: tuple[ECSEstimate, ...] = (
    ECSEstimate(
        label="IPCC AR6 assessed best estimate (all lines of evidence)",
        ecs_c=AR6_ECS_BEST_ESTIMATE_C,
        range_c=AR6_ECS_LIKELY_RANGE_C,
        citation="IPCC AR6 WG1 (2021), Summary for Policymakers.",
        leans="moderate",
    ),
    ECSEstimate(
        label="Myers et al. 2021 (low-cloud feedback constraint)",
        ecs_c=None,
        range_c=None,
        citation=MYERS_2021_CITATION,
        leans="moderate",
    ),
    ECSEstimate(
        label="Tan et al. 2025 (opposing mixed-phase cloud feedbacks)",
        ecs_c=TAN_2025_ECS_C,
        range_c=(
            TAN_2025_ECS_C - TAN_2025_ECS_UNCERTAINTY_1SIGMA_C,
            TAN_2025_ECS_C + TAN_2025_ECS_UNCERTAINTY_1SIGMA_C,
        ),
        citation=TAN_2025_CITATION,
        leans="moderate",
    ),
    ECSEstimate(
        label="2025/2026 cloud-controlling-factor analyses (observed-pattern-matched models)",
        ecs_c=None,
        range_c=None,
        citation=(
            "Multiple 2025/2026 studies (e.g. Geophysical Research Letters) "
            "constraining models against observed historical low-cloud "
            "behavior; see HIGHER_SENSITIVITY_NOTE in constants.py."
        ),
        leans="higher",
    ),
)


def moderate_leaning_estimates() -> tuple[ECSEstimate, ...]:
    return tuple(e for e in ALL_ECS_ESTIMATES if e.leans == "moderate")


def higher_leaning_estimates() -> tuple[ECSEstimate, ...]:
    return tuple(e for e in ALL_ECS_ESTIMATES if e.leans == "higher")


def is_genuinely_disputed() -> bool:
    """True if estimates lean in more than one direction -- an honest,
    structural check rather than a hardcoded claim."""
    directions = {e.leans for e in ALL_ECS_ESTIMATES}
    return len(directions) > 1
