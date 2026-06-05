"""Workflow orchestration for MOSAICA pipelines."""

from typing import Any, Dict


class WorkflowManager:
    """Manage execution flows and pipeline steps."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def run_preprocessing(self) -> Any:
        """Execute the preprocessing stage."""
        raise NotImplementedError("WorkflowManager.run_preprocessing must be implemented.")

    def run_optimization(self) -> Any:
        """Execute the optimization stage."""
        raise NotImplementedError("WorkflowManager.run_optimization must be implemented.")

    def run_simulation(self) -> Any:
        """Execute the GAMA simulation stage."""
        raise NotImplementedError("WorkflowManager.run_simulation must be implemented.")

