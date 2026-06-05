"""Objective functions for MOSAICA optimization."""

from typing import Any, Dict


class ObjectiveFunction:
    """Base class for objective functions."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def evaluate(self, decision_variables: Any) -> float:
        """Evaluate the objective for given decision variables."""
        raise NotImplementedError("ObjectiveFunction.evaluate must be implemented.")


class RevenueObjective(ObjectiveFunction):
    """Maximize agricultural revenue."""

    def evaluate(self, decision_variables: Any) -> float:
        raise NotImplementedError("RevenueObjective.evaluate must be implemented.")

