# config_loader.py
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]


def load_config(path: str) -> dict:
    config_path = BASE_DIR / "config" / path
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg


def resolve_file(cfg, path: str) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return cfg["data_dir"] / p
