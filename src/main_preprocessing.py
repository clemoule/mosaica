# src/main.py

from preprocessing.dataset_builder import build_datasets
from preprocessing.compute_parameters import build_parameters
from preprocessing.merge_datasets import build_global_datasets
from preprocessing.registry import create_registry

from src.shared.config_loader import load_config


def main():

    # =====================================================
    # CONFIG
    # =====================================================

    cfg = load_config("preprocessing_config.yaml")

    mappings = load_config("config_mappings.yaml")

    # =====================================================
    # RAW DATASETS
    # =====================================================

    raw_datasets, raw_registry = build_datasets(cfg)

    # =====================================================
    # PARAMETERS
    # =====================================================

    parameter_datasets = build_parameters(
        raw_datasets,
        mappings
    )

    parameter_registry = create_registry(
        parameter_datasets,
        "parameters"
    )

    # =====================================================
    # GLOBAL DATASETS
    # =====================================================

    global_datasets = build_global_datasets(
        raw_datasets,
        parameter_datasets
    )

    global_registry = create_registry(
        global_datasets,
        "global"
    )

    # =====================================================
    # CONCAT REGISTRY
    # =====================================================

    full_registry = raw_registry.copy()

    full_registry["dataset_type"] = "raw"

    full_registry = full_registry[[
        "dataset_type",
        "variable",
        "rows",
        "cols",
        "columns"
    ]]

    parameter_registry.columns = full_registry.columns
    global_registry.columns = full_registry.columns

    full_registry = pd.concat([
        full_registry,
        parameter_registry,
        global_registry
    ])

    print(full_registry)

    return {
        "raw": raw_datasets,
        "parameters": parameter_datasets,
        "global": global_datasets,
        "registry": full_registry
    }


if __name__ == "__main__":
    main()