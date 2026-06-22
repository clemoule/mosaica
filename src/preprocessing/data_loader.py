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

    # =========================
    # CSV
    # =========================
    if suffix == ".csv":
        df = try_read(path)

        if df is not None:
            return df

    # =========================
    # TXT / SET
    # =========================
    if suffix in [".txt", ".set"]:
        attempts = [
            # séparateur auto
            dict(sep=None, engine="python"),
            # espaces multiples
            dict(sep=r"\s+", engine="python"),
            # tabulations
            dict(sep="\t", engine="python"),
            # point-virgule
            dict(sep=";", engine="python"),
            # virgule
            dict(sep=",", engine="python"),
            # ultra permissif
            dict(sep=r"\s+", engine="python", on_bad_lines="skip"),
        ]

        for params in attempts:
            df = try_read(path, **params)

            if df is not None and len(df.columns) > 0:
                return df

    raise ValueError(f"Impossible de parser : {path}")
