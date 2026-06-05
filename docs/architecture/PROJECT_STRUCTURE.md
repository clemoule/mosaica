# Project Structure

Ce document d�crit l'arborescence du projet MOSAICA apr�s restructuration.

## Racine du projet

- `README.md` : pr�sentation du projet et orientation.
- `pyproject.toml` : configuration du package Python principal et source de vérité des dépendances.
- `docker/` : configuration Docker de la plateforme.
- `src/` : modules numérotés pour le pipeline Python et GAMA.
- `tests/` : tests unitaires et d'int�gration.
- `docs/` : documentation projet et architecture.
- `inputs/`, `logs/`, `outputs/` : entrées, journaux et résultats.

## `src/`

Contient les modules de traitement et de simulation organisés par étapes :

- `src/1_preprocessing/` : preprocessing des données et préparation d'entrées.
- `src/2_maelia_pipeline/` : pipeline de génération des inputs et exécution MAELIA.
- `src/3_optimisation/` : optimisation multi-critère.
- `src/4_orchestration/` : orchestration des workflows.
- `src/5_analysis_visualization/` : analyse et visualisation des scénarios.
- `src/6_gama_multiagent/` : modèle multi-agent GAMA / MAELIA.

## `src/1_preprocessing/`

Contient la partie preprocessing du projet :

- `main.py` : entrée dédiée au preprocessing.
- `preprocessing/` : modules de nettoyage, GIS et dataset.
- `preprocessing_config.yaml` : configuration dédiée de preprocessing.

## `src/2_maelia_pipeline/`

Contient le pipeline MAELIA du projet :

- `main.py` : entrée dédiée au pipeline MAELIA.
- `gama_interface/` : interface avec GAMA / MAELIA.
- `maelia_pipeline_config.yaml` : configuration dédiée du pipeline.

## `src/3_optimisation/`

Contient la partie optimisation du projet :

- `main.py` : entrée dédiée à l'optimisation.
- `optimization/` : modules d'optimisation et solveurs.
- `optimisation_config.yaml` : configuration dédiée de l'optimisation.

## `src/4_orchestration/`

Contient l'orchestration du workflow :

- `main.py` : entrée dédiée à l'orchestration.
- `orchestration/` : modules de coordination et de lancement.
- `orchestration_config.yaml` : configuration dédiée de l'orchestration.

## `src/5_analysis_visualization/`

Contient la partie analyse et visualisation :

- `main.py` : entrée dédiée à l'analyse/visualisation.
- `analysis/` : post-traitement, métriques et scoring.
- `visualization/` : graphiques et rapports.
- `analysis_visualization_config.yaml` : configuration dédiée.

## `src/6_gama_multiagent/`

Contient la partie GAMA / MAELIA multi-agent :

- `main.py` : entrée dédiée au modèle GAMA multi-agent.
- `gaml/` : modèles GAMA et paramètres.
- `gama_multiagent_config.yaml` : configuration dédiée du modèle.

## Principes de modularit� et de non-redondance

- `src/` contient les modules numérotés et découplés. Python orchestre, optimise et gère les pipelines; GAMA exécute la simulation dans `src/6_gama_multiagent/`.
- Les variables sont centralisées par module dans chaque dossier `src/*` avec des configs dédiées.
- `docker/` reste si Docker est utilisé pour l'exécution de GAMA.
- `inputs/` remplace `data/` pour les entrées.
- `pyproject.toml` est la source principale de vérité pour le packaging et les dépendances.

## Recommandations

- Ne pas dupliquer les variables d'environnement dans plusieurs fichiers.
- Chaque dossier numéroté possède sa propre config YAML locale.
- Garder la documentation de l'architecture dans `docs/architecture/` et ne pas disperser cette logique dans des fichiers racine.
