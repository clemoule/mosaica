# src/preprocessing/merge_datasets.py

import pandas as pd


def build_global_datasets(raw: dict, params: dict):

    global_datasets = {}

    # =====================================================
    # PARCELLE GLOBAL
    # =====================================================

    parc_global = raw["data_parc_gwad_2017"].merge(
        params["parc_features"],
        on="SP",
        how="left",
        suffixes=("", "_PARAM")
    )

    global_datasets["parc_global"] = parc_global

    return global_datasets