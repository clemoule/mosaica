"""Unit tests for utils module."""

import pytest
from pathlib import Path
import tempfile
import json
import pandas as pd

from mosaica.utils import (
    resolve_path, validate_path, validate_dataframe, 
    read_json, write_json, read_csv, write_csv
)


class TestPathUtils:
    """Test path utilities."""
    
    def test_resolve_path_absolute(self):
        """Test resolving absolute path."""
        abs_path = Path('/absolute/path')
        result = resolve_path(abs_path)
        assert result == abs_path
    
    def test_resolve_path_relative(self, tmp_path):
        """Test resolving relative path."""
        rel_path = Path('relative/path')
        result = resolve_path(rel_path)
        assert result.is_absolute()
    
    def test_validate_path_exists(self, tmp_path):
        """Test validating existing path."""
        test_file = tmp_path / 'test.txt'
        test_file.touch()
        
        assert validate_path(test_file, must_exist=True) is True
    
    def test_validate_path_not_exists(self, tmp_path):
        """Test validating non-existing path."""
        test_file = tmp_path / 'nonexistent.txt'
        
        with pytest.raises(FileNotFoundError):
            validate_path(test_file, must_exist=True)


class TestValidators:
    """Test validators."""
    
    def test_validate_dataframe_valid(self, sample_dataframe):
        """Test validating valid DataFrame."""
        assert validate_dataframe(sample_dataframe) is True
    
    def test_validate_dataframe_invalid(self):
        """Test validating invalid DataFrame."""
        with pytest.raises(ValueError):
            validate_dataframe("not a dataframe")
    
    def test_validate_dataframe_min_rows(self, sample_dataframe):
        """Test DataFrame validation with minimum rows."""
        assert validate_dataframe(sample_dataframe, min_rows=4) is True
        
        with pytest.raises(ValueError):
            validate_dataframe(sample_dataframe, min_rows=10)


class TestIOHandlers:
    """Test I/O handlers."""
    
    def test_write_and_read_json(self, tmp_path):
        """Test writing and reading JSON."""
        data = {'key': 'value', 'number': 42}
        path = tmp_path / 'test.json'
        
        write_json(data, path)
        result = read_json(path)
        
        assert result == data
    
    def test_write_and_read_csv(self, tmp_path, sample_dataframe):
        """Test writing and reading CSV."""
        path = tmp_path / 'test.csv'
        
        write_csv(sample_dataframe, path, index=False)
        result = read_csv(path)
        
        assert result.shape == sample_dataframe.shape
        assert list(result.columns) == list(sample_dataframe.columns)

