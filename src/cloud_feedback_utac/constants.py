"""Real, independently verified constants for cloud-feedback-utac (P89).

Checked 2026-08-02. Deliberately has NO UTAC/CREP/AFET bridge -- per
Johann's climate-topic guidance. See DISCLAIMER.md.
"""

from __future__ import annotations

PACKAGE_ID = 89

# -- Background (real, IPCC AR6) ----------------------------------------------
CLOUD_FEEDBACK_NOTE = (
    "Low marine clouds strongly cool the planet by reflecting sunlight. How "
    "this cooling responds to warming is the leading source of uncertainty "
    "in equilibrium climate sensitivity (ECS) -- the eventual warming from "
    "doubling atmospheric CO2."
)

# -- IPCC AR6 ECS assessment (real, well established) ------------------------
AR6_ECS_BEST_ESTIMATE_C = 3.0
AR6_ECS_LIKELY_RANGE_C = (2.5, 4.0)  # likely (>=66%), high confidence
AR6_ECS_VERY_LIKELY_RANGE_C = (2.0, 5.0)  # very likely (>=90%), medium confidence

# -- Myers et al. 2021 (real, moderate-sensitivity anchor) -------------------
MYERS_2021_CITATION = (
    "Myers, T.A., Scott, R.C., Zelinka, M.D., Klein, S.A., Norris, J.R., "
    "Caldwell, P.M. (2021). \"Observational constraints on low cloud "
    "feedback reduce uncertainty of climate sensitivity\". Nature Climate "
    "Change, 11(6), 501-507. DOI: 10.1038/s41558-021-01039-0."
)
MYERS_2021_LOW_CLOUD_FEEDBACK_WM2_PER_K = 0.19
MYERS_2021_LOW_CLOUD_FEEDBACK_UNCERTAINTY_WM2_PER_K = 0.12  # 90% CI
"""Near-global marine low-cloud feedback -- positive (amplifying), but the
paper's constraint narrows uncertainty toward MODERATE climate sensitivity
(~3 K), not toward the high end of the AR6 range."""

# -- Tan et al. 2025 (real, moderate-sensitivity via opposing mechanisms) ----
TAN_2025_CITATION = (
    "Tan, I., Zhou, C., Lamy, A., Stauffer, C.L. (2025). \"Moderate climate "
    "sensitivity due to opposing mixed-phase cloud feedbacks\". npj Climate "
    "and Atmospheric Science, 8, article 86."
)
TAN_2025_ECS_C = 3.63
TAN_2025_ECS_UNCERTAINTY_1SIGMA_C = 0.98
"""Constrains individual climate models' mixed-phase-cloud representation
against satellite observations; finds a moderate resulting ECS because
increasing cloud-liquid fraction (amplifying) and increasing reflective
cloud cover (dampening) partly cancel."""

# -- Real, current (2025/2026) higher-sensitivity findings (genuine disagreement) --
HIGHER_SENSITIVITY_NOTE = (
    "Separately, other real 2025/2026 studies (cloud-controlling-factor "
    "analyses constrained against observed historical cloud patterns, e.g. "
    "in Geophysical Research Letters) find that models best matching "
    "observed low-cloud behavior project STRONGER positive low-cloud "
    "feedback and correspondingly HIGHER climate sensitivity than the "
    "moderate estimates above. This is a genuine, current, unresolved "
    "scientific disagreement about which observational constraint method "
    "is more reliable -- not a settled question either way."
)
