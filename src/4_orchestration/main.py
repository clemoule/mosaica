from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "orchestration_config.yaml"


def main():
    print("[4_orchestration] Start orchestration stage")
    print(f"Using config: {CONFIG_PATH}")


if __name__ == "__main__":
    main()
