"""I/O handlers for MOSAICA."""

import json
from pathlib import Path
from typing import Any, Dict, Union

import pandas as pd


def read_json(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Read JSON file.
    
    Args:
        path: Path to JSON file
        
    Returns:
        Dictionary from JSON
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: Dict[str, Any], path: Union[str, Path], indent: int = 2) -> None:
    """
    Write dictionary to JSON file.
    
    Args:
        data: Dictionary to write
        path: Output path
        indent: JSON indentation
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


def read_csv(path: Union[str, Path], **kwargs) -> pd.DataFrame:
    """
    Read CSV file.
    
    Args:
        path: Path to CSV file
        **kwargs: Additional arguments for pd.read_csv()
        
    Returns:
        DataFrame
    """
    return pd.read_csv(path, **kwargs)


def write_csv(df: pd.DataFrame, path: Union[str, Path], **kwargs) -> None:
    """
    Write DataFrame to CSV file.
    
    Args:
        df: DataFrame to write
        path: Output path
        **kwargs: Additional arguments for pd.to_csv()
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, **kwargs)

