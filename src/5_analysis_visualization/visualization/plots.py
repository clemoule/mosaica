"""Visualization helpers for MOSAICA outputs."""

from typing import Any, Dict


class PlotBuilder:
    """Build plots for optimization and simulation outputs."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def plot_pareto_front(self, data: Any) -> Any:
        """Plot a Pareto front from optimization results."""
        raise NotImplementedError("PlotBuilder.plot_pareto_front must be implemented.")

    def plot_spatial_map(self, geodata: Any) -> Any:
        """Render a spatial map from GeoDataFrames or raster outputs."""
        raise NotImplementedError("PlotBuilder.plot_spatial_map must be implemented.")

