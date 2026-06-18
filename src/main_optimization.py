# src/main_optimization.py

from src.shared.config_loader import load_config
from preprocessing.dataset_builder import build_datasets
from preprocessing.compute_parameters import build_features
from model.optimization import build_model
from model.solver import solve_model
import pyomo.environ as pyo


def main():

    cfg = load_config()

    datasets, _ = build_datasets(cfg)

    features = build_features(datasets)

    model = build_model(features)

    result = solve_model(model)

    print("Optimisation terminée")


if __name__ == "__main__":
    main()

