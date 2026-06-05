from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "preprocessing_config.yaml"


def main():
    print("[1_preprocessing] Start preprocessing stage")
    print(f"Using config: {CONFIG_PATH}")


if __name__ == "__main__":
    main()
