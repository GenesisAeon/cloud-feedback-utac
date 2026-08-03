# cloud-feedback-utac

[![GenesisAeon](https://img.shields.io/badge/GenesisAeon-P89-blue)](https://github.com/GenesisAeon)
[![CI](https://github.com/GenesisAeon/cloud-feedback-utac/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/cloud-feedback-utac/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21780592.svg)](https://doi.org/10.5281/zenodo.21780592)

GenesisAeon Package 89 — real cloud-feedback / climate-sensitivity science.
**Deliberately has no UTAC/CREP/AFET bridge** — see
[DISCLAIMER.md](DISCLAIMER.md).

## What's real here

- IPCC AR6's assessed equilibrium climate sensitivity (ECS): best estimate
  3.0°C, likely range 2.5-4.0°C.
- Myers et al. (2021, *Nature Climate Change*): observational constraint
  on low-cloud feedback narrowing toward moderate sensitivity.
- Tan et al. (2025, *npj Climate and Atmospheric Science*): moderate ECS
  (3.63±0.98°C) from opposing mixed-phase cloud feedback mechanisms.
- **A genuine, current, unresolved disagreement**: separate real
  2025/2026 observational-constraint studies find *higher* sensitivity.
  Both sides are represented honestly — `is_genuinely_disputed()` exists
  specifically so this isn't silently resolved to a false single answer.

## Quickstart

```bash
pip install cloud-feedback-utac
```

```python
from cloud_feedback_utac import is_genuinely_disputed, ALL_ECS_ESTIMATES

print(f"Genuinely disputed: {is_genuinely_disputed()}")
for est in ALL_ECS_ESTIMATES:
    print(f"{est.label} ({est.leans}): {est.citation}")
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
