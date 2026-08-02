"""cloud-feedback-utac -- GenesisAeon Package 89.

Real cloud-feedback / climate-sensitivity science. Deliberately has NO
UTAC/CREP/AFET bridge -- per climate-topic guidance. See DISCLAIMER.md.
"""

from cloud_feedback_utac.constants import (
    AR6_ECS_BEST_ESTIMATE_C,
    AR6_ECS_LIKELY_RANGE_C,
    AR6_ECS_VERY_LIKELY_RANGE_C,
    CLOUD_FEEDBACK_NOTE,
    HIGHER_SENSITIVITY_NOTE,
    MYERS_2021_CITATION,
    MYERS_2021_LOW_CLOUD_FEEDBACK_WM2_PER_K,
    PACKAGE_ID,
    TAN_2025_CITATION,
    TAN_2025_ECS_C,
)
from cloud_feedback_utac.estimates import (
    ALL_ECS_ESTIMATES,
    ECSEstimate,
    higher_leaning_estimates,
    is_genuinely_disputed,
    moderate_leaning_estimates,
)

__version__ = "1.0.0"

__all__ = [
    "PACKAGE_ID",
    "CLOUD_FEEDBACK_NOTE",
    "AR6_ECS_BEST_ESTIMATE_C",
    "AR6_ECS_LIKELY_RANGE_C",
    "AR6_ECS_VERY_LIKELY_RANGE_C",
    "MYERS_2021_CITATION",
    "MYERS_2021_LOW_CLOUD_FEEDBACK_WM2_PER_K",
    "TAN_2025_CITATION",
    "TAN_2025_ECS_C",
    "HIGHER_SENSITIVITY_NOTE",
    "ECSEstimate",
    "ALL_ECS_ESTIMATES",
    "moderate_leaning_estimates",
    "higher_leaning_estimates",
    "is_genuinely_disputed",
    "__version__",
]
