from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "analysis_visualization_config.yaml"


def main():
    print("[5_analysis_visualization] Start analysis and visualization stage")
    print(f"Using config: {CONFIG_PATH}")


if __name__ == "__main__":
    main()
