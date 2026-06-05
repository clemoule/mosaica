"""Validators for MOSAICA."""

import pandas as pd
import geopandas as gpd


def validate_dataframe(df: pd.DataFrame, min_rows: int = 0) -> bool:
    """
    Validate a pandas DataFrame.
    
    Args:
        df: DataFrame to validate
        min_rows: Minimum number of rows required
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If validation fails
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Object is not a pandas DataFrame")
    
    if len(df) < min_rows:
        raise ValueError(f"DataFrame has {len(df)} rows, minimum {min_rows} required")
    
    return True


def validate_geodataframe(gdf: gpd.GeoDataFrame, must_have_crs: bool = True) -> bool:
    """
    Validate a geopandas GeoDataFrame.
    
    Args:
        gdf: GeoDataFrame to validate
        must_have_crs: If True, must have CRS defined
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If validation fails
    """
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise ValueError("Object is not a geopandas GeoDataFrame")
    
    if must_have_crs and gdf.crs is None:
        raise ValueError("GeoDataFrame must have a CRS defined")
    
    if not all(gdf.geometry.is_valid):
        raise ValueError("GeoDataFrame contains invalid geometries")
    
    return True


def validate_numeric_range(value: float, min_val: float, max_val: float) -> bool:
    """
    Validate a numeric value is within range.
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If out of range
    """
    if not (min_val <= value <= max_val):
        raise ValueError(f"Value {value} not in range [{min_val}, {max_val}]")
    return True

