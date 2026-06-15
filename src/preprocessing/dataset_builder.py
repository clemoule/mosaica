# dataset_builder.py
import pandas as pd
from pathlib import Path
from preprocessing.data_loader import load_file
from preprocessing.config_loader import resolve_file


def build_datasets(cfg):
    datasets_cfg = cfg["datasets"]
    registry = []

    loaded = {}

    for var_name, file_rel in datasets_cfg.items():
        path = resolve_file(cfg, file_rel)

        df = load_file(path)

        loaded[var_name] = df

        registry.append({
            "variable": var_name,
            "file": str(path),
            "rows": df.shape[0],
            "cols": df.shape[1],
            "columns": list(df.columns) if df.shape[1] > 0 else []
        })

    registry_df = pd.DataFrame(registry)

    return loaded, registry_df


def export_parquet(loaded: dict, cfg):
    out_dir = Path(cfg["paths"]["output_folder"])
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, df in loaded.items():
        df.to_parquet(out_dir / f"{name}.parquet", index=False)