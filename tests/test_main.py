"""Tests for cloud-feedback-utac."""

from __future__ import annotations

from cloud_feedback_utac import (
    ALL_ECS_ESTIMATES,
    AR6_ECS_BEST_ESTIMATE_C,
    AR6_ECS_LIKELY_RANGE_C,
    TAN_2025_ECS_C,
    __version__,
    higher_leaning_estimates,
    is_genuinely_disputed,
    moderate_leaning_estimates,
)


def test_version() -> None:
    assert __version__ == "1.0.0"


def test_ar6_best_estimate_within_likely_range() -> None:
    low, high = AR6_ECS_LIKELY_RANGE_C
    assert low <= AR6_ECS_BEST_ESTIMATE_C <= high


def test_tan_2025_is_moderate_like_ar6() -> None:
    # Tan et al. 2025's ECS is close to, not wildly divergent from, AR6.
    assert abs(TAN_2025_ECS_C - AR6_ECS_BEST_ESTIMATE_C) < 1.0


class TestEstimates:
    def test_all_estimates_have_citations(self) -> None:
        for est in ALL_ECS_ESTIMATES:
            assert est.citation

    def test_all_estimates_have_a_lean(self) -> None:
        for est in ALL_ECS_ESTIMATES:
            assert est.leans in {"moderate", "higher"}

    def test_moderate_and_higher_both_present(self) -> None:
        assert len(moderate_leaning_estimates()) >= 1
        assert len(higher_leaning_estimates()) >= 1

    def test_is_genuinely_disputed(self) -> None:
        # Honest finding: real, current research disagrees on direction.
        assert is_genuinely_disputed() is True

    def test_range_is_ordered_when_present(self) -> None:
        for est in ALL_ECS_ESTIMATES:
            if est.range_c is not None:
                assert est.range_c[0] <= est.range_c[1]
