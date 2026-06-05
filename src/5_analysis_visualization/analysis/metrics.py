"""Analysis metrics for MOSAICA results."""

from typing import Any, Dict


class MetricsCalculator:
    """Compute post-processing metrics and indicators."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def compute_scores(self, results: Any) -> Dict[str, float]:
        """Compute scoring metrics from optimization or simulation outputs."""
        raise NotImplementedError("MetricsCalculator.compute_scores must be implemented.")

    def compare_scenarios(self, baseline: Any, alternative: Any) -> Dict[str, Any]:
        """Compare two scenario results and return metrics."""
        raise NotImplementedError("MetricsCalculator.compare_scenarios must be implemented.")

