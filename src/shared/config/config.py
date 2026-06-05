"""Configuration management for MOSAICA project."""

import logging
from pathlib import Path
from typing import Any, Dict

import yaml

logger = logging.getLogger(__name__)


class Config:
    """
    Centralized configuration management.
    
    Loads configuration from YAML files and provides
    access to project settings.
    
    Example:
        >>> config = Config.load('src/1_preprocessing/preprocessing_config.yaml')
        >>> data_path = config.get('inputs.raw_data_path')
        >>> data_path = config.get('inputs.raw_data_path', 'inputs/default')
    """
    
    def __init__(self, config_dict: Dict[str, Any]):
        """Initialize Config with a dictionary."""
        self._config = config_dict
        self._logger = logging.getLogger(self.__class__.__name__)
    
    @classmethod
    def load(cls, *config_paths: str) -> 'Config':
        """
        Load configuration from one or more YAML files.
        
        Args:
            *config_paths: Paths to YAML configuration files.
            
        Returns:
            Config instance
            
        Raises:
            FileNotFoundError: If any config file doesn't exist
            yaml.YAMLError: If YAML is malformed
        """
        config_dict: Dict[str, Any] = {}

        for config_path in config_paths:
            path = Path(config_path)
            if not path.exists():
                raise FileNotFoundError(f"Config file not found: {config_path}")

            with open(path, 'r', encoding='utf-8') as f:
                current_config = yaml.safe_load(f)

            if current_config is None:
                current_config = {}

            config_dict = cls._merge_dicts(config_dict, current_config)

        return cls(config_dict)

    @staticmethod
    def _merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Merge two dictionaries recursively."""
        result = base.copy()
        for key, value in override.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = Config._merge_dicts(result[key], value)
            else:
                result[key] = value
        return result
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'data.input_path')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
            
        Example:
            >>> config.get('data.input_path', 'inputs/')
            '/absolute/path/to/inputs'
        """
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'data.input_path')
            value: Value to set
        """
        keys = key.split('.')
        current = self._config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """Get entire configuration as dictionary."""
        return self._config.copy()
    
    def validate(self) -> bool:
        """
        Validate configuration completeness.
        
        Returns:
            True if all required keys present
        """
        required_keys = ['data', 'optimization', 'gama']
        for key in required_keys:
            if key not in self._config:
                self._logger.warning(f"Missing required config key: {key}")
                return False
        return True
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Config({len(self._config)} keys)"

