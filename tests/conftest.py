"""Pytest configuration and shared fixtures."""

import pytest
from pathlib import Path
import tempfile
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "value": [10.5, 20.3, 15.7, 22.1, 18.9],
            "category": ["A", "B", "A", "C", "B"],
        }
    )


@pytest.fixture
def sample_geodataframe():
    """Create a sample GeoDataFrame for testing."""
    geometries = [
        Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
        Polygon([(1, 0), (2, 0), (2, 1), (1, 1)]),
        Polygon([(0, 1), (1, 1), (1, 2), (0, 2)]),
    ]

    gdf = gpd.GeoDataFrame(
        {
            "id": [1, 2, 3],
            "name": ["parcel_1", "parcel_2", "parcel_3"],
            "area": [1.0, 1.0, 1.0],
            "geometry": geometries,
        },
        crs="EPSG:4326",
    )

    return gdf


@pytest.fixture
def config_dict():
    """Create a sample configuration dictionary."""
    return {
        "data": {
            "input_path": "/inputs/input",
            "output_path": "/inputs/output",
            "crs_target": "EPSG:2970",
        },
        "optimization": {
            "algorithm": "NSGA-III",
            "n_generations": 100,
            "population_size": 150,
        },
        "gama": {
            "mode": "docker",
            "timeout_seconds": 3600,
        },
        "logging": {
            "level": "INFO",
        },
    }


@pytest.fixture
def allocation_dict():
    """Create a sample allocation dictionary."""
    return {
        "parcel_1": {"crop": "maize", "area_ha": 0.8},
        "parcel_2": {"crop": "cassava", "area_ha": 0.95},
        "parcel_3": {"crop": "banana", "area_ha": 0.75},
    }


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "slow: marks tests as slow")
