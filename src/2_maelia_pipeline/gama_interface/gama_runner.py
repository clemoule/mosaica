"""GAMA / MAELIA coupling runner."""

from pathlib import Path
from typing import Any, Dict


class GamaRunner:
    """Launch and monitor GAMA simulations."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def prepare_input(self, directory: Path) -> None:
        """Write model input files for GAMA."""
        raise NotImplementedError("GamaRunner.prepare_input must be implemented.")

    def run_simulation(self) -> Any:
        """Run the GAMA simulation and return results."""
        raise NotImplementedError("GamaRunner.run_simulation must be implemented.")

    def extract_output(self, directory: Path) -> Any:
        """Read simulation output and convert to Python objects."""
        raise NotImplementedError("GamaRunner.extract_output must be implemented.")

