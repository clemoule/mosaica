# main.py
from preprocessing.config_loader import load_config
from preprocessing.dataset_builder import build_datasets, export_parquet
from preprocessing.dataset import MosaicDataset


def main():
    # 1. Charger config YAML
    cfg = load_config()

    # 2. Construire tous les datasets + registry
    loaded, registry = build_datasets(cfg)

    print("\n✔ Registry construit")
    print(registry.head())

    # 3. Export parquet (optionnel mais recommandé)
    if cfg["settings"].get("export_parquet", False):
        export_parquet(loaded, cfg)
        print("\n✔ Parquet exporté")

    # 4. Construire dataset global (si usage ML / PyTorch)
    dataset = MosaicDataset(loaded)

    print("\n✔ Dataset prêt")
    print("Nb variables:", len(dataset))

    # 5. Exemple d'accès
    key, df = dataset[0]
    print("\nExemple variable:", key)
    print(df.shape)


if __name__ == "__main__":
    main()