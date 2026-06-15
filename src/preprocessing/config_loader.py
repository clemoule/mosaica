# config_loader.py
import yaml
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[2]

def load_config(path: str = "preprocessing_config.yaml"):

    config_path = BASE_DIR / "config" / path
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # override data_dir si variable d'env existe
    if "MOSAICA_DATA_DIR" in os.environ:
        cfg["data_dir"] = os.environ["MOSAICA_DATA_DIR"]

    cfg["data_dir"] = Path(cfg["data_dir"]).resolve()

    return cfg


def resolve_file(cfg, file_path: str) -> Path:
    p = Path(file_path)
    if p.is_absolute():
        return p
    return cfg["data_dir"] / p