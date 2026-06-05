"""Unit tests for Config module."""

import pytest
from pathlib import Path
import tempfile
import yaml

from mosaica.config import Config


class TestConfig:
    """Test Config class."""
    
    def test_config_load_from_yaml(self, tmp_path):
        """Test loading config from YAML file."""
        config_data = {
            'data': {'input_path': '/inputs/input'},
            'optimization': {'algorithm': 'NSGA-III'},
        }
        
        config_file = tmp_path / 'config.yaml'
        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)
        
        config = Config.load(str(config_file))
        assert config.get('data.input_path') == '/inputs/input'
        assert config.get('optimization.algorithm') == 'NSGA-III'
    
    def test_config_get_with_default(self, config_dict):
        """Test getting config value with default."""
        config = Config(config_dict)
        
        # Existing key
        assert config.get('data.input_path') == '/inputs/input'
        
        # Non-existing key with default
        assert config.get('nonexistent.key', 'default_value') == 'default_value'
    
    def test_config_set(self, config_dict):
        """Test setting config value."""
        config = Config(config_dict)
        
        config.set('data.new_key', 'new_value')
        assert config.get('data.new_key') == 'new_value'
    
    def test_config_to_dict(self, config_dict):
        """Test converting config to dictionary."""
        config = Config(config_dict)
        result = config.to_dict()
        
        assert result == config_dict
        assert isinstance(result, dict)
    
    def test_config_validate(self, config_dict):
        """Test config validation."""
        config = Config(config_dict)
        assert config.validate() is True
    
    def test_config_missing_file(self):
        """Test loading non-existent config file."""
        with pytest.raises(FileNotFoundError):
            Config.load('/nonexistent/path/config.yaml')

