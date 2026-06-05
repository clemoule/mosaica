"""GIS data loading and raster preparation."""

from pathlib import Path
from typing import Any, Dict


class SIGDataLoader:
    """Load and validate GIS vector and raster data."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def load_shapefile(self, path: Path) -> Any:
        """Load a shapefile and return a GeoDataFrame."""
        raise NotImplementedError("SIGDataLoader.load_shapefile must be implemented.")

    def harmonize_crs(self, data: Any, target_crs: str) -> Any:
        """Transform a GeoDataFrame to the target CRS."""
        raise NotImplementedError("SIGDataLoader.harmonize_crs must be implemented.")


class RasterProcessor:
    """Raster data processing utilities."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def load_raster(self, path: Path) -> Any:
        """Load a raster dataset from disk."""
        raise NotImplementedError("RasterProcessor.load_raster must be implemented.")

    def reproject_raster(self, raster: Any, target_crs: str) -> Any:
        """Reproject raster data to a target CRS."""
        raise NotImplementedError("RasterProcessor.reproject_raster must be implemented.")

