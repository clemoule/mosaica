"""Spatial operations for vector and raster datasets."""

from typing import Any


class SpatialOperations:
    """Encapsulate spatial joins and overlay operations."""

    def __init__(self) -> None:
        pass

    def point_in_polygon_join(self, points: Any, polygons: Any) -> Any:
        """Perform a point-in-polygon join."""
        raise NotImplementedError(
            "SpatialOperations.point_in_polygon_join must be implemented."
        )

    def intersect(self, layer_a: Any, layer_b: Any) -> Any:
        """Intersect two spatial layers."""
        raise NotImplementedError("SpatialOperations.intersect must be implemented.")

    def calculate_area(self, geometries: Any) -> Any:
        """Calculate geometry areas."""
        raise NotImplementedError("SpatialOperations.calculate_area must be implemented.")

