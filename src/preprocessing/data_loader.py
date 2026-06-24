# data_loader.py

import pandas as pd
from pathlib import Path


def try_read(path, **kwargs):
    try:
        return pd.read_csv(path, **kwargs)
    except Exception:
        return None


def load_file(path: Path) -> pd.DataFrame:

    suffix = path.suffix.lower()

    if suffix == ".csv":
        df = try_read(path)
        if df is not None:
            return df

    if suffix in [".txt", ".set"]:
        attempts = [
            dict(sep=None, engine="python"), # séparateur auto
            dict(sep=r"\s+", engine="python"), # espaces multiples
            dict(sep="\t", engine="python"), # tabulations
            dict(sep=";", engine="python"), # point-virgule
            dict(sep=",", engine="python"), # virgule
            dict(sep=r"\s+", engine="python", on_bad_lines="skip"), # ultra permissif
        ]

        for params in attempts:
            df = try_read(path, **params)
            if df is not None and len(df.columns) > 0:
                return df

    raise ValueError(f"Impossible de parser : {path}")
