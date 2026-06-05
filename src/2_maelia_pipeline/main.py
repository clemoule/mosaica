from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "maelia_pipeline_config.yaml"


def main():
    print("[2_maelia_pipeline] Start MAELIA pipeline stage")
    print(f"Using config: {CONFIG_PATH}")


if __name__ == "__main__":
    main()
