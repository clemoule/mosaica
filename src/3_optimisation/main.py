from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "optimisation_config.yaml"


def main():
    print("[3_optimisation] Start optimisation stage")
    print(f"Using config: {CONFIG_PATH}")


if __name__ == "__main__":
    main()
