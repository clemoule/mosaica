"""Path utilities for MOSAICA."""

from pathlib import Path
from typing import Union


def resolve_path(path: Union[str, Path]) -> Path:
    """
    Resolve a path to absolute form.
    
    Args:
        path: Path as string or Path object
        
    Returns:
        Absolute Path object
    """
    p = Path(path)
    if p.is_absolute():
        return p
    return p.resolve()


def validate_path(path: Union[str, Path], must_exist: bool = False) -> bool:
    """
    Validate if a path exists.
    
    Args:
        path: Path to validate
        must_exist: If True, path must exist
        
    Returns:
        True if valid
        
    Raises:
        FileNotFoundError: If path doesn't exist and must_exist=True
    """
    p = Path(path)
    if must_exist and not p.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    return True


def ensure_dir(path: Union[str, Path]) -> Path:
    """
    Ensure directory exists, creating if necessary.
    
    Args:
        path: Directory path
        
    Returns:
        Path object
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

