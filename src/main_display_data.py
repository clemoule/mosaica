from preprocessing.dataset_builder import build_datasets
from shared.config_loader import load_config


def main():

    cfg = load_config("preprocessing.yaml")

    raw_datasets, raw_registry = build_datasets(cfg)
    print("\nRegistry:")
    print(raw_registry)
    return {"raw": raw_datasets, "registry": raw_registry}


if __name__ == "__main__":
    main()
