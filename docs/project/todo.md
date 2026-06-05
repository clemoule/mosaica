# MOSAICA Project Task Tracker

## Status Legend

- 🔴 Not Started
- 🟡 In Progress
- 🟢 Completed
- ⏸️ On Hold

---

# Phase 1: Architecture & Foundation

## 1.1 Restructuration du repository

- [ ] 🔴 Create `src/` with numbered modules
- [ ] 🔴 Create `src/1_preprocessing/`, `src/2_maelia_pipeline/`, `src/3_optimisation/`, `src/4_orchestration/`, `src/5_analysis_visualization/`, `src/6_gama_multiagent/`
- [ ] 🔴 Create `tests/{unit, integration}`
- [ ] 🔴 Create `docs/{architecture, api, tutorials}`
- [ ] 🔴 Create `experiments/` notebook directory
- [ ] 🔴 Organize GAML models into `src/6_gama_multiagent/gaml`

## 1.2 Configuration de base

- [ ] 🔴 Create `pyproject.toml` with all dependencies
- [ ] 🔴 Remove `.env.example` and use direct environment configuration if needed
- [ ] 🔴 Create `src/shared/config/__init__.py`
- [ ] 🔴 Create `src/shared/config/config.py`
- [ ] 🔴 Update `.gitignore`

## 1.3 Documentation architecture

- [ ] 🔴 Create `docs/architecture/00_ARCHITECTURE_OVERVIEW.md`
- [ ] 🔴 Create `docs/architecture/01_PYTHON_MODULES.md`
- [ ] 🔴 Create `docs/architecture/02_GAML_STRUCTURE.md`
- [ ] 🔴 Create `docs/architecture/03_DATA_FLOW.md`
- [ ] 🔴 Create `docs/project/contributing.md`

## 1.4 CI/CD & tooling

- [ ] 🔴 Create `.github/workflows/tests.yml`
- [ ] 🔴 Setup `black`, `isort`, `pylint`, `mypy`
- [ ] 🔴 Create `.pre-commit-config.yaml`

---

# Phase 2: Infrastructure Python

## 2.1 Module de configuration

- [ ] 🔴 Create shared config loader in `src/shared/config/config.py`
- [ ] 🔴 Create unit tests for config
- [ ] 🔴 Create per-module config files under each `src/*` folder

## 2.2 Module de logging & monitoring

- [ ] 🔴 Create `src/shared/config/logging_config.py`
- [ ] 🔴 Create `src/shared/utils/performance.py`
- [ ] 🔴 Create tests for logging

## 2.3 Module utilitaires

- [ ] 🔴 Create `src/shared/utils/path_utils.py`
- [ ] 🔴 Create `src/shared/utils/validators.py`
- [ ] 🔴 Create `src/shared/utils/io_handlers.py`
- [ ] 🔴 Create tests for utils

## 2.4 Tests de foundation

- [ ] 🔴 Setup `pytest` fixtures
- [ ] 🔴 Create `tests/unit/test_config.py`
- [ ] 🔴 Create `tests/unit/test_utils.py`

---

# Phase 3: Preprocessing SIG

## 3.1 Module SIG de base

- [ ] 🔴 Create `src/1_preprocessing/preprocessing/gis_loader.py`
- [ ] 🔴 Create `src/1_preprocessing/preprocessing/spatial_operations.py`
- [ ] 🔴 Create `src/1_preprocessing/preprocessing/data_cleaning.py`
- [ ] 🔴 Create unit tests for preprocessing

## 3.2 Data set construction

- [ ] 🔴 Create `src/1_preprocessing/preprocessing/dataset_builder.py`
- [ ] 🔴 Create `src/1_preprocessing/preprocessing/agricultural_params.py`
- [ ] 🔴 Create `src/1_preprocessing/preprocessing/constraints.py`
- [ ] 🔴 Create `src/1_preprocessing/preprocessing/export_handlers.py`

---

# Phase 4: Optimization and coupling

## 4.1 Optimization framework

- [ ] 🔴 Create `src/3_optimisation/optimization/optimization_model.py`
- [ ] 🔴 Create `src/3_optimisation/optimization/objectives.py`
- [ ] 🔴 Create `src/3_optimisation/optimization/pymoo_solver.py`
- [ ] 🔴 Create `src/3_optimisation/optimization/calibration.py`
- [ ] 🔴 Create `src/3_optimisation/optimization/solution_analysis.py`

## 4.2 GAMA / MAELIA integration

- [ ] 🔴 Create `src/2_maelia_pipeline/gama_interface/gama_runner.py`
- [ ] 🔴 Create `src/2_maelia_pipeline/gama_interface/io_adapter.py`
- [ ] 🔴 Create integration tests

## 4.3 Orchestration

- [ ] 🔴 Create `src/4_orchestration/orchestration/workflow.py`
- [ ] 🔴 Create `src/4_orchestration/orchestration/experiment_manager.py`

---

# Phase 5: Analysis & visualization

- [ ] 🔴 Create `src/5_analysis_visualization/analysis/metrics.py`
- [ ] 🔴 Create `src/5_analysis_visualization/analysis/statistics.py`
- [ ] 🔴 Create `src/5_analysis_visualization/visualization/plots.py`
- [ ] 🔴 Create `src/5_analysis_visualization/visualization/maps.py`

---

# Notes

Mettez à jour ce fichier régulièrement pour refléter l'avancement réel du projet.
