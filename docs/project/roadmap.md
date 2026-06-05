# MOSAICA Project Roadmap

## Overview

Ce document présente la feuille de route complète d'implémentation du projet MOSAICA ↔ MAELIA ↔ Multi-Agent.

## Phase 1 : Architecture & Foundation (Semaine 1-2)

### 1.1 Restructuration du repository

- Créer structure `src/{1_preprocessing, 2_maelia_pipeline, 3_optimisation, 4_orchestration, 5_analysis_visualization, 6_gama_multiagent}`
- Créer `tests/{unit, integration}`
- Créer `docs/{architecture, api, tutorials}`
- Créer `experiments/`
- Créer des fichiers de config par module dans `src/*`
- Organiser GAML models dans `src/6_gama_multiagent/gaml`

### 1.2 Configuration de base

- Créer `pyproject.toml`
- Supprimer la dépendance à `.env.example` et documenter les variables d'environnement locales requises
- Créer `src/shared/config/__init__.py` et `src/shared/config/config.py`
- Créer des fichiers de config modulaires sous `src/*`

### 1.3 Documentation architecture

- Créer `docs/architecture/00_ARCHITECTURE_OVERVIEW.md`
- Créer `docs/architecture/01_PYTHON_MODULES.md`
- Créer `docs/architecture/02_GAML_STRUCTURE.md`
- Créer `docs/architecture/03_DATA_FLOW.md`

### 1.4 CI/CD & tooling

- Créer `.github/workflows/tests.yml`
- Configurer linting (`pylint`, `black`)
- Configurer `mypy`

## Phase 2 : Infrastructure Python (Semaine 2-3)

### 2.1 Module de configuration

- Créer `src/shared/config/config.py`
- Gérer les chemins d'entrées `inputs/`, chemins GAMA et paramètres d'optimisation
- Support YAML/JSON

### 2.2 Module de logging & monitoring

- Configurer logging structuré
- Créer loggers par module

### 2.3 Module utilitaires

- Fonctions de conversion paths
- Validateurs d'entrée
- Sérialisation JSON / GeoJSON

### 2.4 Tests de foundation

- Configurer `pytest`
- Créer fixtures communes
- Tests pour `config` et `utils`

## Phase 3 : Preprocessing SIG (Semaine 3-4)

### 3.1 Module SIG de base

- `SIGDataLoader` pour charger shapefiles
- `RasterProcessor` pour données raster
- Harmonisation CRS
- Validation géométrique

### 3.2 Module de jointures spatiales

- Jointures points / polygones
- Intersection raster / vecteur
- Calcul de surfaces
- Opérations d'overlay

### 3.3 Module nettoyage de données

- Gestion valeurs manquantes
- Détection outliers
- Validation des plages

### 3.4 Tests preprocessing

- Tests unitaires et d'intégration
- Fixtures GeoDataFrame

## Phase 4 : Construction du dataset (Semaine 4-5)

- `DatasetBuilder`
- Paramètres agricoles
- Contraintes
- Export CSV / GeoJSON / JSON

## Phase 5 : Framework d'optimisation (Semaine 5-7)

- `OptimizationModel`
- `ObjectiveFunction`
- `PyMOOSolver`
- Calibration
- Analyse de solutions

## Phase 6 : Interface GAMA / MAELIA

- Couplage des entrées/sorties
- Lancement de simulations
- Extraction de résultats

## Phase 7 : Orchestration

- Pipeline de calcul
- Gestion d'expériences
- Reprise et batch processing

## Phase 8 : Analyse & post-processing

- Calcul d'indicateurs
- Comparaison de scénarios
- Validation de robustesse

## Phase 9 : Visualisation

- Graphiques, cartes, dashboards
- Présentation des fronts de Pareto
- Comparaison spatiale

## Phase 10 : Tests & validation

- Couverture ≥80%
- Tests unitaires, d'intégration et d'acceptance

## Phase 11 : Documentation

- Documentation architecture
- Tutoriels
- API
- Guides de déploiement

## Phase 12 : DevOps & déploiement

- CI/CD
- Docker
- Packaging
- Reproductibilité
