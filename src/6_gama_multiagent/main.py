from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "gama_multiagent_config.yaml"


def main():
    print("[6_gama_multiagent] Start GAMA multi-agent stage")
    print(f"Using config: {CONFIG_PATH}")
    print(f"GAML model path: {Path(__file__).parent / 'gaml' / 'main.gaml'}")


if __name__ == "__main__":
    main()
